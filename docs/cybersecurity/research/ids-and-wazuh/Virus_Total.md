---
sidebar_position: 25
---

:::important

By **Prabhgun Singh**. **16/09/2024**

:::

# Change to Wazuh Manager

docker exec -it single-node-wazuh.manager-1 /bin/bash

/var/ossec/etc/ossec.conf

# Code
```
<integration>
<name>virustotal</name>
<api_key>insert </api_key>
<group>syscheck</group>
<alert_format>json</alert_format>
</integration>
```

# Restart Manager

/var/ossec/bin/wazuh-control restart

# Rules for Wazuh agent

Yuhan@redback

/var/ossec/etc/ossec.conf in Wazuh agent

# Code

```
<syscheck>
<directories check_all="yes"
realtime="yes">/home/virustotaltest</directories>
</syscheck>
```

# systemctl restart wazuh-agent

Make a directory inside home - virustest

sudo curl -Lo /media/user/software/suspicious-file.exe https://secure.eicar.org/eicar.com

# Output in Wazuh Manager

![Wazuh](img\Virus1.png)

![Wazuh](img\Virus2.png)

![Wazuh](img\Virus3.png)

![Wazuh](img\Virus4.png)

![Wazuh](img\Virus5.png)