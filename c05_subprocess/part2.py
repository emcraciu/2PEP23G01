class Utils:

    def get_ip_adress(self):
        result = subprocess.Popen(['ipconfig'], text=True, stdout=subprocess.PIPE)
        output = result.communicate()[0]
        matches = re.finditer(r'(Ethernet|Wireless)(\s\w+)+', output)
        interfaces = []
        for match in matches:
            interfaces.append(match.group())
        ip_matches = re.finditer(r"disconnected|(?<=(Address. . . . . . . . . . . : ))(\d+\.)+\d+", output)
        ip_addresses = []
        for ip_match in ip_matches:
            ip_addresses.append(ip_match.group())
        dict = {interfaces[i]: ip_addresses[i] for i in range(len(interfaces))}
        return dict