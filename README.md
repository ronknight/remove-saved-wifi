<h1 align="center">📶 <a href="https://github.com/ronknight/remove-saved-wifi">Remove Saved WiFi</a></h1>

<h4 align="center">🔧 A Python-based utility to list and delete saved WiFi networks from Windows systems.</h4>

<p align="center">
  <a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
  <a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
  <a href="https://github.com/ronknight/remove-saved-wifi/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
  <a href="https://github.com/ronknight/remove-saved-wifi/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
  <a href="https://github.com/ronknight/remove-saved-wifi/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
  <a href="https://github.com/ronknight/remove-saved-wifi/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

---

## 📑 Table of Contents

<p align="center">
  <a href="#project-overview">Project Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## 📖 Project Overview

The **Remove Saved WiFi** script is a Python-based tool that simplifies the process of managing WiFi profiles on Windows systems. It allows users to list all saved WiFi profiles and delete unused or insecure profiles via a simple terminal interface. It uses the `netsh` command-line utility built into Windows.

---

## ✨ Features

- Retrieve a list of all saved WiFi profiles.
- Interactively choose and delete a specific WiFi profile.
- Safe and lightweight with no external dependencies.
- Easy to use on Windows command line or terminal.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ronknight/remove-saved-wifi.git
   cd remove-saved-wifi
   ```

2. **Ensure Python is Installed**:
   - This script requires **Python 3.x**.
   - Verify your Python installation:
     ```bash
     python --version
     ```

3. **Run the Script**:
   No external libraries are required. You can directly execute the script:
   ```bash
   python remove_wifi.py
   ```

---

## 🚀 Usage

### Step-by-Step Instructions

1. **List Saved WiFi Profiles**:
   Run the script, and it will display all saved WiFi profiles on your Windows system:
   ```bash
   python remove_wifi.py
   ```
   Example output:
   ```
   Fetching saved Wi-Fi profiles...

   Saved Wi-Fi Profiles:
   1. HomeWiFi
   2. OfficeWiFi
   3. CafeHotspot
   ```

2. **Remove a WiFi Profile**:
   When prompted, choose the number corresponding to the WiFi profile you want to remove:
   ```
   Enter the number of the Wi-Fi profile to remove (or 0 to cancel): 2
   Successfully removed Wi-Fi profile: OfficeWiFi
   ```

3. **Cancel Operation**:
   To cancel without making changes, simply enter `0` at the prompt.

---

## 🛠️ How It Works

### Code Walkthrough

1. **List WiFi Profiles**:
   - The script uses the `netsh wlan show profiles` command to retrieve a list of all saved WiFi profiles.
   - It parses the output to extract profile names.

2. **Delete WiFi Profile**:
   - The `netsh wlan delete profile name=<WiFi_Profile_Name>` command is used to remove the specified WiFi profile from the system.

3. **Interactive User Input**:
   - After listing profiles, the script prompts the user to choose a profile by its index for deletion.
   - Input validation ensures that invalid or out-of-range inputs are safely handled.

### Sample Code
```python
def list_wifi_profiles():
    result = subprocess.run(
        ["netsh", "wlan", "show", "profiles"],
        stdout=subprocess.PIPE,
        text=True,
    )
    profiles = []
    for line in result.stdout.splitlines():
        if "All User Profile" in line:
            profile_name = line.split(":")[1].strip()
            profiles.append(profile_name)
    return profiles
```

---

## 🤝 Contributing

Contributions are welcome! If you encounter bugs or have ideas for improvements, follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add your feature"
   ```
4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a **pull request** on GitHub.

---

## ⚖️ License

This project is licensed under the **MIT License**. For more details, see the [LICENSE](https://github.com/ronknight/remove-saved-wifi/blob/master/LICENSE) file.

---

## ⚠️ Disclaimer

This script modifies system configurations. Use it carefully to avoid unintended disconnections or profile deletions. Ensure you have administrative privileges and double-check profile names before deletion.