import json
import os
import platform
import urllib.request


def get_system():
    system = platform.system()
    if system == "Linux" or system == "Windows":
        return system
    elif system == "Darwin":
        return "macOS"
    else:
        raise ValueError(f"Unsupported system: {system}")


print("setting installer variables")
version = "2022.2.1"
system = get_system()
request = urllib.request.Request("https://w-bonelli.github.io/assets/json/oneapi.json")
response = urllib.request.urlopen(request, timeout=10)
result = json.loads(response.read().decode())
cpp_url = result[system][version]["cpp"]
ftn_url = result[system][version]["ftn"]

with open(os.environ.get("GITHUB_ENV"), "a") as env_file:
    env_file.write(f"INTEL_CPP_COMPILER_INSTALLER_URL={cpp_url}{os.linesep}")
    env_file.write(f"INTEL_FTN_COMPILER_INSTALLER_URL={cpp_url}{os.linesep}")
    env_file.write(f"INTEL_COMPILER_VERSION={version}{os.linesep}")
