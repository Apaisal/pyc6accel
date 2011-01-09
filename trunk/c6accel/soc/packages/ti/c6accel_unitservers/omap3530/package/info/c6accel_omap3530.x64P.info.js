{
    "DSP memory map": [
        [
            "L4PER",
            {
                "addr": 0x49000000,
                "type": "other",
                "size": 0x00100000,
            },
        ],
        [
            "DDR2",
            {
                "addr": 0x87D00000,
                "type": "main",
                "size": 0x00300000,
            },
        ],
        [
            "IRAM",
            {
                "addr": 0x107F8000,
                "type": "code",
                "size": 0x00008000,
                "gppAddr": 0x5C7F8000,
            },
        ],
        [
            "L1DSRAM",
            {
                "addr": 0x10F04000,
                "type": "code",
                "size": 0x00010000,
                "gppAddr": 0x5CF04000,
            },
        ],
        [
            "RESET_VECTOR",
            {
                "addr": 0x87300000,
                "type": "reset",
                "size": 0x00001000,
            },
        ],
        [
            "DDRALGHEAP",
            {
                "addr": 0x87400000,
                "type": "other",
                "size": 0x00900000,
            },
        ],
        [
            "L4CORE",
            {
                "addr": 0x48000000,
                "type": "other",
                "size": 0x01000000,
            },
        ],
        [
            "DSPLINKMEM",
            {
                "addr": 0x87301000,
                "type": "link",
                "size": 0x000FF000,
            },
        ],
        [
            "CMEM",
            {
                "addr": 0,
                "type": "other",
                "size": 0,
            },
        ],
    ],
    "server algorithms": {
        "programName": "c6accel_omap3530.x64P",
        "algs": [
            {
                "mod": "ti.c6accel.ce.C6ACCEL",
                "pkg": "ti.c6accel.ce",
                "rpcProtocolVersion": 1,
                "ialgFxns": "C6ACCEL_TI_IC6ACCEL",
                "threadAttrs": {
                    "priority": 4,
                },
                "groupId": 2,
                "serverFxns": "UNIVERSAL_SKEL",
                "stubFxns": "UNIVERSAL_STUBS",
                "name": "c6accel",
                "pkgVersion": [
                    "1, 0, 0",
                ],
            },
        ],
    },
}
