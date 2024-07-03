import json

# Config map
config_map = {}

# Get the symbols we care about, the .. ones are double pointers
# and we handle that later
config_symbols = [
    i for i in bv.symbols if "_main/config" in i and "_main/config.." not in i
]

for i in config_symbols:
    sym_addr = bv.get_symbols_by_name(i)[0]
    data_var = bv.get_data_var_at(sym_addr.address)

    # I think this only happens once??
    if data_var is None:
        continue

    # There are two primary field types we care about, void* and int64_t
    # probably should switch on the actual type enum val but this works for now
    match str(data_var.type):
        case "void*":
            ptr_addr = data_var.value
            next_ptr = bv.get_symbol_at(ptr_addr)

            # Handle case where pointer points to another pointer
            # (handle the config.. from earlier)
            if (
                next_ptr is not None
                and "config" in next_ptr.name
                and "gobytes" not in next_ptr.name
            ):
                print(
                    f"ptr at {hex(ptr_addr)} with name {bv.get_symbol_at(ptr_addr).name}"
                )
                n_data_var = bv.get_data_var_at(next_ptr.address)
                str_offset = n_data_var.value

                # The length of the string is the next int64
                # following the pointer
                str_size = bv.read_int(ptr_addr + 0x8, 0x4)
            else:
                str_offset = ptr_addr
                str_size = bv.read_int(sym_addr.address + 0x8, 0x4)

            # There are some junk values in the config
            # that are REALLY big so we truncate them for pretty printing
            trunk = lambda truncated_str: (
                truncated_str[:300] + "..."
                if len(truncated_str) > 300
                else truncated_str
            )

            # Split the symbol and add to the config map
            config_map[i.split(".")[-1]] = trunk(
                bv.read(str_offset, str_size).decode("utf8")
            )

        case "char" | "int64_t":
            config_map[i.split(".")[-1]] = data_var.value
        case _:
            # Gonna relook at this cause there might be some
            # other types, but this gets most of the important
            # stuff.
            pass

print(json.dumps(config_map, indent=4))
