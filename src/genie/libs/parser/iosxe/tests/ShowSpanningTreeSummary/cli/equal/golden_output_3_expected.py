expected_output = {
    'bpdu_filter': False,
    'bpdu_guard': True,
    'configured_pathcost': {
        'method': 'short',
    },
    'etherchannel_misconfig_guard': True,
    'extended_system_id': True,
    'loop_guard': False,
    'mode': {
        'rapid_pvst': {
            'VLAN0001': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0002': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0003': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0004': {
                'blocking': 0,
                'forwarding': 6,
                'learning': 0,
                'listening': 0,
                'stp_active': 6,
            },
            'VLAN0005': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0006': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0007': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0008': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
            'VLAN0009': {
                'blocking': 0,
                'forwarding': 5,
                'learning': 0,
                'listening': 0,
                'stp_active': 5,
            },
        },
    },
    'portfast_default': True,
    'root_bridge_for': 'VLAN0001, VLAN0002, VLAN0003, VLAN0004, VLAN0005, VLAN0006, VLAN0007, VLAN0008, VLAN0009',
    'total_statistics': {
        'blockings': 0,
        'forwardings': 46,
        'learnings': 0,
        'listenings': 0,
        "num_of_vlans": 9,
        'stp_actives': 46,
    },
}