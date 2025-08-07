import json, os

class ConfigManager:
    def __init__(self, config_path="preferences.json"):
        self.config_path = config_path
        self.config = {
            "default_source": "",
            "default_dest": "",
            "zip_by_default": False
        }
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                self.config.update(json.load(f))

    def save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()
