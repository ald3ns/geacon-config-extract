# Geacon Config Extraction Binja Script

Geacon is a Cobalt Strike implementation written in Go. There are two versions that can be found on Github:

- https://github.com/darkr4y/geacon
- https://github.com/Z3ratu1/geacon_plus

This script will use the symbols present in builds that haven't been obfuscated using a tool like [garble](https://github.com/burrowers/garble]) to dump the config (see [geacon source](https://github.com/Z3ratu1/geacon_plus/blob/main/config/config.go)). Obviously, that means this script is brittle, but it is entirely possible the config is found in the same place each time.

The sample this script was tested with was: https://www.virustotal.com/gui/file/cc210ecd2d8b8060eb272fd37b65e1eb00d4cfb65795a82299d89a01df56ea7d.

It will probably work more generically but I haven't tested much yet. To run this, just use the `Run Script..` functionality in Binary Ninja.

## Quick Note

A more interesting recent sample was: https://www.virustotal.com/gui/file/1a162c9b3d47f64994a6b0efa766c2ff46845d720921825122a82340809d4ecd.
It's garbled so this script won't work but it was part of an interesting DMG called `CloudPrinterSetupNew_c5u5wg.dmg`.

It shares a number of similarities with the [sample analyzed](https://www.sentinelone.com/blog/geacon-brings-cobalt-strike-capabilities-to-macos-threat-actors/) by Phil Stokes and Dinesh Devadoss in May of 2023.
