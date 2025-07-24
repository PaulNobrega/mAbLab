import json

def mab_to_json(mab):
    """
    Serialize a fully constructed Mab object to a JSON-compatible dict.
    """
    def safe(obj):
        # Helper to safely serialize objects, handling None and basic types
        if obj is None:
            return None
        if isinstance(obj, (str, int, float, bool)):
            return obj
        if isinstance(obj, list):
            return [safe(i) for i in obj]
        if isinstance(obj, dict):
            return {k: safe(v) for k, v in obj.items()}
        # For objects, get their __dict__ and recursively serialize
        if hasattr(obj, "__dict__"):
            return {k: safe(v) for k, v in obj.__dict__.items() if not k.startswith("_")}
        return str(obj)

    mab_dict = {
        "hc1": safe(mab.hc1),
        "hc2": safe(mab.hc2),
        "lc1": safe(mab.lc1),
        "lc2": safe(mab.lc2),
        "fab1": safe(mab.fab1),
        "fab2": safe(mab.fab2),
        "properties": safe(mab.properties),
        "errors": safe(getattr(mab, "errors", None)),
    }
    return mab_dict

# Example usage:
# from mAbLab import Mab
# HC = "EVQLVESGGGLVQPGRSLRLSCAASGFTFDDYAMHW..."  # truncated for example
# LC = "DIQMTQSPSSLSASVGDRVTITCRASQGIRNYLAW..."  # truncated for example
# mab = Mab(hc1_aa_sequence=HC, hc2_aa_sequence=HC, lc1_aa_sequence=LC, lc2_aa_sequence=LC)
# print(json.dumps(mab_to_json(mab), indent=2))
