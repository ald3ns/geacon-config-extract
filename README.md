# Geacon Config Extraction Binja Script

Geacon is a Cobalt Strike implementation written in Go. There are two versions that can be found on Github:

- https://github.com/darkr4y/geacon
- https://github.com/Z3ratu1/geacon_plus

This script will use the symbols present in builds that haven't been obfuscated using a tool like [garble](https://github.com/burrowers/garble]) to dump the config (see [geacon source](https://github.com/Z3ratu1/geacon_plus/blob/main/config/config.go)). Obviously, that means this script is brittle, but it is entirely possible the config is found in the same place each time.

The sample this script was tested with was: https://www.virustotal.com/gui/file/cc210ecd2d8b8060eb272fd37b65e1eb00d4cfb65795a82299d89a01df56ea7d.

It will probably work more generically but I haven't tested much yet. To run this, just use the `Run Script..` functionality in Binary Ninja.

The output should look something like this:

```
{
    "GetClientPrepend": "id=ARBIT7_",
    "GetClientAppend": "-PRcealq0PBjVoUQ",
    "MetaDataFieldType": "header",
    "MetaDataField": "Cookie",
    "GetServerPrepend": "#EXTM3U #EXT-X-VERSION:7 #EXT-X-INDEPENDENT-SEGMENTS  #-- en (3) -- #EXT-X-MEDIA:TYPE=AUDIO,LANGUAGE=\"en\",GROUP-ID=\"audio-HE2-stereo-32\",NAME=\"English\",DEFAULT=YES,AUTOSELECT=YES,CHANNELS=\"2\",URI=\"https://apptrailers.itunes.apple.com/itunes-assets/PurpleVideo116/v4/e9/12/80/e912803e-088b-3cf8-95c1-f...",
    "GetServerAppend": "f7c714eb46695697db51c19702f633d2b04d3eeb11421951b58f739fa16b\" https://apptrailers.itunes.apple.com/itunes-assets/PurpleVideo116/v4/a6/b1/a9/a6b1a96d-c5f8-9093-990b-113cb54a256a/P637646201_Anull_video_gr680_sdr_1920x1080.m3u8 #EXT-X-STREAM-INF:AVERAGE-BANDWIDTH=8259459,_AVG-BANDWIDTH=8259459,BANDWIDT...",
    "PostClientIDType": "header",
    "PostClientID": "Cookie",
    "PostClientIDPrepend": "GUID=baefevdadb8f62403b93040d777c",
    "PostClientIDAppend": "7a0db&HASH=baea;",
    "PostClientPrepend": "timezone=Europe/London&dataSets=airQuality&clientMetadata=CgJHQ",
    "PostClientAppend": "hoFZW4tR0JKA",
    "PostServerPrepend": "{\"airQuality\":{\"name\":\"AirQuality\",\"metadata\":{\"attributionURL\":\"https://dynamic-link.breezometer.com/?lat=51.500&lon=-0.167&partner=apple\",\"expireTime\":\"2024-06-02T17:07:02Z\",\"language\":\"en-GB\",\"latitude\":51.500,\"longitude\":-0.167,\"providerName\":\"BreezoMeter\",\"readTime\":\"2024-06-02T17:03:51Z\",\"repo...",
    "PostServerAppend": "23606.82,\"windDirection\":306,\"windGust\":15.34,\"windSpeed\":5.62},{\"forecastStart\":\"2024-06-03T03:00:00Z\",\"cloudCover\":0.68,\"cloudCoverLowAltPct\":0.29,\"cloudCoverMidAltPct\":0.54,\"cloudCoverHighAltPct\":0.7,\"conditionCode\":\"MostlyCloudy\",\"daylight\":false,\"humidity\":0.86,\"perceivedPrecipitationIntensity\"...",
    "Host": "IP ADDRESS",
    "TimeLayout": "2006-01-02 15:04:05",
    "GetUri": "/itunes-assets/f4ed132e-b37f-9af2fccb098b/P637646201.m3u8",
    "GetMetaEncryptType": "base64url",
    "GetServerEncryptType": "mask",
    "PostClientIDEncrypt": "base64",
    "PostClientDataEncryptType": "base64",
    "PostServerEncryptType": "mask",
    "PostUri": "/v3/weather/en-GB/51.500/-0.167",
    "RsaPublicKey": "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMfuPq9/Ltd0JOjnqOz4Ul4WiUrwcNdZmwoYG2\nNZnlokkJNMmFWdlDHNs/+4QuuvE/CKoAkEsLmNuLzNBMlgr5QxIeKv4W99I9KdWvaaepk6PsEr+0\njKz3mXnqdnJLDkyPe5y+AeXV1SIYr5JcK+Bxc4fpHuEnB0s+GCJ3jBjF2wIDAQAB\n-----END PUBLIC KEY-----",
    "IgnoreSSLVerify": 1,
    "Support41Plus": 1,
    "Debug": 1,
    "TimeOut": 10000000000,
    "WaitTime": 2000,
    "Jitter": 35,
    "MaxRetries": 30,
    "HttpHeadersGet": 0,
    "HttpHeadersPost": 0,
    "HttpHeaders": 0,
    "EndTime": 0,
    "ProxyUrl": 0,
    "HostName": 0,
    "IsDNS": 0
}
```

## Quick Note

A more interesting recent sample was: https://www.virustotal.com/gui/file/1a162c9b3d47f64994a6b0efa766c2ff46845d720921825122a82340809d4ecd.
It's garbled so this script won't work but it was part of an interesting DMG called `CloudPrinterSetupNew_c5u5wg.dmg`.

It shares a number of similarities with the [sample analyzed](https://www.sentinelone.com/blog/geacon-brings-cobalt-strike-capabilities-to-macos-threat-actors/) by Phil Stokes and Dinesh Devadoss in May of 2023.
