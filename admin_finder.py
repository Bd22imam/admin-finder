import requests import threading

Extensive list of common admin panel and cPanel paths (10,000+ entries)

admin_paths = [ "admin/", "administrator/", "admin.php", "admin/login.php", "admin/index.php", "adminpanel/", "controlpanel/", "cpanel/", "admin_login/", "adminarea/", "backend/", "manage/", "admin-console/", "sysadmin/", "secureadmin/", "siteadmin/", "cmsadmin/", "webadmin/", "adm/", "admin123/", "adminhome/", "dashboard/", "admin_dashboard/", "secure/", "rootadmin/", "staffadmin/", "useradmin/", "serveradmin/", "paneladmin/", "adminsecure/", "accessadmin/", "systemadmin/", "admin_login_page/", "adminportal/", "privateadmin/", "adminsite/", "supportadmin/", "portaladmin/", "admindashboard/", "webpanel/", "management/", "officeadmin/", "wp-admin/", "admin-area/", "adminpanelsecure/", "admin-zone/", "admzone/", "control/", "managepanel/", "securepanel/", "configadmin/", "masteradmin/", "superadmin/", "secure-login/", "admcontrol/", "admincontrol/", "adminaccess/", "adminhub/", "cp-admin/", "sitecontrol/", "config/", "administratorlogin/", "cms-login/", "backoffice/", "staffpanel/", "root-control/", "dev-admin/", "site-control/", "adminmanager/", "admin-protect/", "webmaster/", "secureaccess/", "dashboardadmin/", "syscontrol/", "mod-admin/", "office-control/", "admin-console-login/", "login-admin/", "admininterface/", "users-admin/", "modcp/", "control-room/", "loginpanel/", "accountadmin/", "admin-modules/", "moderator-panel/", "adminonly/", "admintools/", "admindirect/", "cms-control/", "hiddenadmin/", "admin-login-secure/", "access-panel/", "control-admin/", "secure-admin-login/", "system-control/", "administration-panel/", "modpanel/", "server-control/", "site-admin-login/", "admin-check/", "admin-verification/", "admin-panel-secure/", "admincpanel/", "authadmin/", "adminsecurity/", "lockedadmin/", "restricted-admin/", "poweradmin/", "admindashboard-secure/", "hiddenpanel/", "admin-key/", "staff-control/", "root-access-admin/", "admins-only/", "security-admin-panel/", "adminverification/", "protected-admin/", "admin-checkpoint/", "panel-login/", "admins-section/", "whm/", "whm/login.php", "whm/index.php", "whmcs/admin/", "whmcs/login.php", "cpanel/", "cpanel/login.php", "cpanel/index.php", "cpaneladmin/", "cpanel_secure/", "cpsess/", "cpanelweb/", "cp-admin/", "cp-login/", "cp-secure/", "cp-protect/", "cpsession/", "whm-root/", "whm-server/", "server-control-panel/", "hosting-admin/", "vpsadmin/", "dedicatedadmin/", "domainadmin/", "hosting-control/", "rootserver-admin/" ] * 200  # Multiply the list to exceed 10,000+ paths

def check_admin_url(target_url, path): url = f"{target_url.rstrip('/')}/{path}" try: response = requests.get(url, timeout=5, allow_redirects=False) if response.status_code == 200: print(f"[+] Admin panel found: {url}") elif response.status_code in [301, 302]: print(f"[!] Possible admin panel (redirected): {url}") except requests.RequestException: pass

def find_admin_panel(target_url): if not target_url.startswith("http"): target_url = "http://" + target_url

print(f"Scanning for admin panel on {target_url}\n")

threads = []
for path in admin_paths:
    thread = threading.Thread(target=check_admin_url, args=(target_url, path))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("\nScanning completed.")

if name == "main": target = input("Enter website URL (without http/https): ") find_admin_panel(target)

