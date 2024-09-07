---
sidebar_position: 13
---
# PHISHING

Phishing is a type of cybercrime that takes advantage of human behavior to trick people into revealing confidential information or downloading harmful software. It remains one of the most common and effective methods employed by cybercriminals to illegally access personal and financial data. The term "phishing" reflects the analogy of fishing, where attackers cast broad nets to ensnare unsuspecting victims.

Phishing attacks often involve deceptive communications that appear to come from legitimate sources, such as financial institutions, online platforms, or trusted entities. Email phishing is the most prevalent form, with attackers sending messages that closely resemble authentic correspondence, encouraging recipients to click on links, provide personal details, or download malicious attachments.

The increasing sophistication of phishing techniques makes it more difficult for individuals and organizations to recognize and defend against these threats. With the rise of social engineering tactics and advanced technologies, attackers can create convincing messages that easily deceive even cautious users.

A notable example of phishing in Australia occurred in 2020 when the Australian Cyber Security Centre (ACSC) reported a surge in phishing attacks during the COVID-19 pandemic. Cybercriminals exploited the crisis by sending emails impersonating health authorities, urging recipients to click on links for information about the virus or to complete personal health forms. This incident highlighted the need for heightened awareness and proactive measures against phishing threats.

Understanding the nature of phishing, its various forms, and preventive measures is essential for safeguarding sensitive information and ensuring cybersecurity. By promoting awareness and best practices, both individuals and organizations can better protect themselves against this widespread threat.

## How Phishing Works

Phishing involves a series of deliberate steps that exploit deception and manipulation to target victims. Understanding this process can help individuals recognize and defend against phishing attacks. Here’s a breakdown of how a typical phishing attack unfolds:

1. **Preparation and Targeting**: Attackers start by identifying their potential victims. This may involve collecting information such as email addresses, job roles, and affiliations. They often utilize social media and other online resources to gather insights about their targets, making their messages more credible.

2. **Crafting the Message**: After pinpointing the target, attackers create a fraudulent message that appears to come from a legitimate source. This could be a bank, government agency, or well-known online service. The messages often use urgent language to provoke quick action, compelling the recipient to respond without careful consideration.

3. **Delivery**: The phishing email is sent to the victim. Attackers may employ various strategies to evade spam filters and ensure their messages reach inboxes. This can involve using legitimate email addresses, spoofing sender information, or leveraging botnets to disseminate phishing emails on a large scale.

4. **Engagement**: When the target receives the email, they may be prompted to click on a link or download an attachment. The link typically directs the victim to a counterfeit website that mimics the legitimate site of the impersonated organization. Here, victims may be asked to provide sensitive information, such as usernames, passwords, or financial details.

5. **Exploitation**: If the target is deceived and submits their information, the attacker captures this data for malicious purposes. This can result in unauthorized access to the victim's accounts, identity theft, or financial fraud. In some instances, downloading an infected attachment may lead to the installation of malware on the victim’s device.

6. **Maintaining Access**: Once the attacker has obtained the victim's information, they may establish ongoing access to the victim’s accounts or systems, allowing them to exploit the stolen credentials further or launch additional attacks on the victim's contacts.

7. **Further Attacks**: With access to the victim’s data, attackers can engage in various malicious activities, such as stealing money, sending more phishing emails to the victim's contacts, or selling the stolen information on the dark web.

## Email Phishing

Email phishing is a cyber-attack method that involves sending fraudulent emails designed to deceive recipients into revealing sensitive information, such as usernames, passwords, or financial details. These emails often appear to come from reputable sources, such as banks, online services, or trusted organizations, making them seem legitimate. Phishing emails typically include urgent messages prompting the recipient to click on a link or download an attachment, leading them to fake websites or installing malware. The primary goal of email phishing is to manipulate individuals into providing their personal information or compromising their systems, which attackers can then exploit for various malicious purposes. Understanding email phishing is crucial, especially for practical exercises aimed at identifying and defending against such attacks.

## Tools for Email Phishing

1. **Gophish**  
   Gophish is a user-friendly, open-source phishing framework that allows users to create and manage phishing campaigns. It provides an intuitive interface for designing emails and tracking engagement, making it ideal for ethical phishing simulations and security training.

2. **Social-Engineering Toolkit (SET)**  
   The Social-Engineering Toolkit (SET) is an open-source framework for penetration testing that simulates social engineering attacks, particularly phishing. It enables security professionals to create realistic phishing emails and replicate websites for credential harvesting, helping organizations assess their defenses against such threats. With its user-friendly interface, SET is widely used in penetration testing and security training. Always obtain proper authorization before use to avoid legal issues.

## How it Works:

![picture1](img/picture1.png)

### Email Phishing: A Systematic Analysis

**Introduction**: Email phishing remains a significant threat in the realm of cybersecurity. This paper aims to elucidate the step-by-step process through which these attacks are conducted, providing insights into their methodology and potential impact.

**Methodology**: The email phishing process typically follows a structured approach:

1. **Email Fabrication**: Attackers craft deceptive emails that closely mimic legitimate communications from trusted entities such as financial institutions or popular online services.

2. **Mass Distribution**: These fraudulent emails are disseminated to a large number of potential victims, often utilizing stolen or purchased email lists.

3. **Urgency Creation**: The content of these emails often incorporates language designed to instill a sense of urgency, compelling recipients to take immediate action.

4. **Malicious Link Inclusion**: A critical component of these emails is the inclusion of a hyperlink that directs users to a fraudulent website.

5. **Fraudulent Website Construction**: The linked website is meticulously designed to replicate the appearance and functionality of legitimate sites, enhancing the deception.

6. **Data Acquisition**: When users input sensitive information into these fraudulent sites, it is immediately captured by the attackers.

7. **Information Exploitation**: The collected data is subsequently utilized for various malicious purposes, including identity theft and financial fraud.

## PRACTICAL USAGE OF SOCIAL ENGINEERING TOOLKIT (SET):

Here is a demonstration of how setoolkit is used to do credential harvesting:

![picture2](img/picture2.png)

### SET Interface

![picture3](img/picture3.png)

The demonstration begins with the Social-Engineering Toolkit (SET) interface displayed in Kali Linux. This user-friendly tool provides various options for executing social engineering attacks, making it accessible for users to select specific attack types. The intuitive layout enables quick navigation through the toolkit’s features.

- **Key features**:
  - Offers multiple attack vectors.
  - Facilitates the selection of specific phishing methods.

### Website Attack Vectors

![picture4](img/picture4.png)

After launching SET, the first action is to select "Website Attack Vectors." This option is crucial for initiating a phishing attack, as it enables the user to create or exploit a website. By choosing this option, I set the stage for simulating a real-world attack scenario.

- **Importance**:
  - Allows for cloning legitimate websites.
  - Essential for executing phishing attacks.

### Credential Harvester Attack Method
![picture5](img/picture5.png)

Following the selection of website attack vectors, the next step involves choosing the "Credential Harvester Attack Method." This method is fundamental for capturing user credentials entered on the cloned site. It showcases how attackers can gather sensitive information by deceiving users into providing their details on a fraudulent page.

- **Significance**:
  - Captures usernames and passwords.
  - Simulates real phishing tactics.

### Entering the IP Address
![picture6](img/picture6.png)

Next, I entered my Kali Linux IP address (192.168.1.120) into SET. This step is critical, as the IP address ensures that any data entered on the cloned site is directed back to my machine. Properly configuring the IP address allows for successful demonstration and analysis of the phishing technique.

- **Purpose**:
  - Directs captured data to the attacker’s machine.
  - Essential for the functionality of the cloned site.

### Cloning the Vulnerable Website
![picture7](img/picture7.png)

The demonstration proceeds with cloning a vulnerable website, specifically http://testphp.vulnweb.com/. This site was chosen for its harmlessness, allowing me to effectively simulate an attack without legal or ethical concerns. Cloning a legitimate login page serves to illustrate how attackers can trick users into entering sensitive information.

- **Chosen site**:
  - http://testphp.vulnweb.com/ for safe demonstration.
  - Mimics real-world phishing scenarios.

### Displaying the Cloned Website
![picture8](img/picture8.png)

Finally, the cloned website is displayed in a web browser. The appearance of the cloned site closely mirrors that of the original, enhancing the realism of the phishing attempt. Any credentials entered on this page would be captured and displayed in the SET interface. This step emphasizes the risks associated with phishing attacks and the importance of user vigilance.

- **Key takeaway**:
  - Cloned site appears authentic, increasing the likelihood of successful phishing.
  - Demonstrates the effectiveness of phishing techniques.

Through this demonstration, I aim to raise awareness about the vulnerabilities present in online security. By showcasing the process of cloning a website and capturing user credentials using SET, I hope to highlight the dangers of phishing attempts and the necessity for individuals to verify the authenticity of websites before entering sensitive information.

## GO PHISH tutorial

GoPhish is an open-source phishing framework for simulating phishing attacks and training cybersecurity teams. It allows the creation of phishing campaigns, custom emails, and landing pages to test user awareness. 

How to use:

![picture9](img/picture9.png)
Creating a Group in GoPhish 
- Log in to your GoPhish dashboard.
- On the left-hand menu, click on Groups.
- Click New Group to create a new group.
- In the Name field, enter the name for your group.
- Manually enter the details for each recipient in the table with columns like First Name, Last Name, Email, and Position.

![picture10](img/picture10.png)
Creating an Email Template in GoPhish 
- Access the GoPhish dashboard.
- From the left menu, select Email Templates.
- Click New Template to start creating a new template.
- Enter a name in the Name field for your email template.
- Input the subject line in the Subject field.
- Use the HTML or Text editor to write the email content, and you can include placeholders for personalized details.
- Attach any files if necessary.
- Click Save Template to finalize and save your template.

![picture11](img/picture11.png)
Creating a Landing Page in GoPhish 
- Go to the GoPhish dashboard.
- Click on Landing Pages in the left menu.
- Select New Landing Page to start.
- Fill in the Name field with a name for your landing page.
- Choose a template or start from scratch.
- Utilize the HTML editor to design your landing page content and add any necessary input fields.
- Click Save Landing Page to save your changes and finish the setup

![picture12](img/picture12.png)
Creating a Sending Profile in GoPhish 
- Navigate to the GoPhish dashboard.
- Click on Sending Profiles in the left sidebar.
- Select New Sending Profile to create a new profile.
- Fill in the Name field with a name for your sending profile.
- Choose the Email Address that will appear as the sender.
- Enter the SMTP Server details:
  - Specify the SMTP server address.
  - Provide the SMTP server port
  - Include the username and password for authentication.
  - If applicable, check the box for Use TLS or Use SSL to secure the connection.
- Click Save Sending Profile to finish creating your profile.


After completing the setup above. Now click on campaign and start a new one. Use the profiles already created and launch a campaign. After launching, the profiles should receive the email with phishing link:
![picture13](img/picture13.png)
