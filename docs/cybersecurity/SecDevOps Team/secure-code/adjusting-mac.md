---
sidebar_position: 10
---

**Last updated by:** T_Apperley, **Last updated on:** 03/12/2024


**Last updated by:** T_Apperley, **Last updated on:** 03/12/2024


# Adjusting MAC address anonymization for the MQTT Manager
Proposed changes for MQTT

:::info
**Author:** Rinor Gimolli
:::

The code, using Python, aims to use data anonymization of client information – more
specifically client names and client MAC addresses. The earlier code did this however, at a
request, the idea was to scramble the MAC address into a alphanumeric ID – with the option
to convert it back.

**Initial Code:**

![Initial Code](img\mac-initial.jpg)

**Code After Changes**

![After Code](img\mac-changes.jpg)

This update hashes the MAC address using MD5, to the encode it in Base64, then it shortens it to 10
characters. This is used to create an alphanumeric ID. Due to these changes, 2 libraries need to be
imported as shown below.

```
import base64
import hashlib
```

Although with these changes reversing to get the original MAC address still isn’t possible, it is still the
most plausible method. For that to happen we would have to convert the hashes into encryption,
which in itself is riskier