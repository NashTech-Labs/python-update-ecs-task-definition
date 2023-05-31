import sys
import json

def get_updated_task_defn(task_defn_file_name, updated_image_tag, updated_env_name):
    with open(task_defn_file_name, 'r') as f:
        data = json.load(f)
        data["containerDefinitions"][0]["image"] = updated_image_tag
        del data["status"]
        del data["registeredAt"]
        del data["registeredBy"]
        del data["requiresAttributes"]
        del data["compatibilities"]
        del data["taskDefinitionArn"]
        del data["revision"]
        data["containerDefinitions"][0]["environment"][0]["value"] = updated_env_name
    return data

def update_task_defn(task_defn_file_name, data):
    with open(task_defn_file_name, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

args = sys.argv[1:]
task_defn_file_name = args[0]
updated_image_tag = args[1]
updated_env_name = args[2]

updated_task_defn = get_updated_task_defn(task_defn_file_name, updated_image_tag, updated_env_name)
update_task_defn(task_defn_file_name, updated_task_defn)
