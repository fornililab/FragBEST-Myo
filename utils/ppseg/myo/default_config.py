import os

LIGAND_FRAG_INFO_PATH = os.path.join(
    os.path.dirname(__file__), "ligand_fragments_example.json"
)

HOLO_DESCRIPTOR_PRESETS = {
    # from apo PPS trajectory (exclude outliers)
    "pps": {
        "overall_predprobs": {"mean": 0.9900573231184204, "std": 0.003032497914663395},
        "nonbck_ratio": {"mean": 0.13142873375206812, "std": 0.06180177467710578},
        "nonbck_class_pt_ratio": {
            "mean": 0.026393200118319343,
            "std": 0.00930172263396527,
        },
        "num_of_classes": {"mean": 5.895392477840773, "std": 1.4010219461838636},
        "num_interest_points": {"mean": 1263.627086161463, "std": 72.40806809698059},
        "holospace_volume": {"mean": 1193.9776147215443, "std": 562.35137723809},
        "holospace_frag_score": {
            "mean": 0.6518119926893339,
            "std": 0.25744573369658225,
        },
    },
    # from apo PR trajectory
    "pr": {
        "overall_predprobs": {"mean": 0.989953240330237, "std": 0.002974217163553127},
        "nonbck_ratio": {"mean": 0.17711210098973174, "std": 0.058945042695694935},
        "nonbck_class_pt_ratio": {
            "mean": 0.03173491381011908,
            "std": 0.008458564608298514,
        },
        "num_of_classes": {"mean": 6.512475538160469, "std": 0.8064857397138876},
        "num_interest_points": {"mean": 1059.159654272668, "std": 63.186565576793065},
        "holospace_volume": {"mean": 1258.5132822056942, "std": 384.9912810536164},
        "holospace_frag_score": {
            "mean": 0.7310062369613581,
            "std": 0.16676280846967548,
        },
    },
}
