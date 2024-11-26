import subprocess

def list_wifi_profiles():
    """
    List all saved Wi-Fi profiles.
    """
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        profiles = []
        for line in result.stdout.splitlines():
            if "All User Profile" in line:
                profile_name = line.split(":")[1].strip()
                profiles.append(profile_name)
        return profiles
    except Exception as e:
        print(f"Error listing Wi-Fi profiles: {e}")
        return []

def delete_wifi_profile(profile_name):
    """
    Remove a specific Wi-Fi profile.
    """
    try:
        subprocess.run(
            ["netsh", "wlan", "delete", "profile", f"name={profile_name}"],
            check=True,
        )
        print(f"Successfully removed Wi-Fi profile: {profile_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove Wi-Fi profile {profile_name}: {e}")

def main():
    """
    Main function to list and remove Wi-Fi profiles.
    """
    print("Fetching saved Wi-Fi profiles...")
    profiles = list_wifi_profiles()
    if not profiles:
        print("No saved Wi-Fi profiles found.")
        return

    print("\nSaved Wi-Fi Profiles:")
    for i, profile in enumerate(profiles, start=1):
        print(f"{i}. {profile}")

    try:
        choice = int(input("\nEnter the number of the Wi-Fi profile to remove (or 0 to cancel): "))
        if choice == 0:
            print("Operation cancelled.")
            return
        elif 1 <= choice <= len(profiles):
            delete_wifi_profile(profiles[choice - 1])
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()
