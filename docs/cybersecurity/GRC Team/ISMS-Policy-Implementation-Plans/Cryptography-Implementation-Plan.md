---
sidebar_position: 4
sidebar_label: Cryptography Implementation Plan 2024
---

# Cryptography Implementation Plan - Redback Operations

**Author:** Ali Demirovski

## Cryptography For Redback Operations

- **Purpose**: Protection and confidentiality of data and files, ensuring the safety of communication, and maintaining authorized access only.

### Encryption Standards:
- **Advanced Encryption Standard (AES)**:
    - Symmetric encryption algorithm, using the same key for both encryption and decryption.
    - One of the most widely used encryption standards globally.

- **ISO/IEC 19790:2012**:
    - This standard outlines how encryption is implemented, including authentication, testing, and configuration management.

- **ISO/IEC 24759:2017**:
    - Covers the impartial testing process of cryptographic modules, ensuring rigorous and unbiased results.

---

## Classification Levels:

### 1. Open/Public:
- Data accessible and editable by anyone.
- No encryption is required for this data classification.

### 2. Private/Confidential:
- Data that is sensitive and limited to authorized personnel.
- Requires encryption to maintain data privacy and security.
- Employees must distinguish between public and private data to ensure correct usage of encryption.

---

## Encryption Software:

### 1. **VeraCrypt**:
- Cost-free encryption software that supports multiple algorithms like AES and Serpent.
- Offers strong protection but may be difficult to use for beginners.

### 2. **BitLocker**:
- Full disk encryption solution for Windows devices.
- Easy to use, but limited to Windows platforms.

### 3. **NordLocker**:
- User-friendly encryption solution supporting both Windows and macOS.
- File-by-file encryption; subscription-based with strong security.

### 4. **AxCrypt**:
- Subscription-based software with a free version for trial.
- Easy to use, offers file-by-file encryption with password protection.

---

## Expected Users and Devices:

- The plan applies company-wide, particularly focusing on developers.
- Devices covered include all company-issued personal devices (laptops, mobile phones) and Raspberry Pi hardware.

---

## Regulatory Compliance:

- Regular audits will ensure that encryption standards are followed.
- Compliance with ISO standards will be key in passing external audits and company reviews.

---

## References:

- **Encryption Standards**:
    - [ISO/IEC 19790:2012](https://www.iso.org/standard/52906.html)
    - [ISO/IEC 24759:2017](https://www.iso.org/standard/72515.html)
    - [Cyber.gov.au Guidelines on Cryptography](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism/cyber-security-guidelines/guidelines-cryptography)
    
- **Encryption Software**:
    - [VeraCrypt](https://sourceforge.net/projects/veracrypt/)
    - [AxCrypt Pricing](https://axcrypt.net/pricing/)
    - [NordLocker](https://nordlocker.com)

