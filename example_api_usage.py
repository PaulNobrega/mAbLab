import json
from mAbLab import Mab

# Construct your Mab object
mab = Mab(hc1_aa_sequence="...", hc2_aa_sequence="...", lc1_aa_sequence="...", lc2_aa_sequence="...")

# Return as JSON for API
json_response = json.dumps(mab.to_dict())
# In a Flask API, you could use: return jsonify(mab.to_dict())
