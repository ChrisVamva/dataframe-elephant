# Security and Privacy as Lifecycle Architecture

> **Vibe:** A smart home is only as trustworthy as its weakest update path, identity boundary, or data practice.

## Core idea

Security is not just encryption or biometrics. It includes authentication, device onboarding, network segmentation, software support, vulnerability handling, privacy controls, and recovery when a vendor or cloud service fails.

## Architecture controls

- Strong account authentication and least-privilege household roles.
- Secure commissioning, authenticated joins, encrypted communications.
- Separate IoT network or VLAN from sensitive computers and accounts.
- Automatic updates, published support periods, retirement and replacement paths.
- Local processing where practical; explicit retention and sharing controls for audio/video.

## Documented developments

NIST recommends planning before purchase, MFA, unique passwords, disabling unused features, privacy review, automatic updates, and network segmentation. The EU Cyber Resilience Act establishes lifecycle cybersecurity requirements for products with digital elements, with major obligations applying from December 2027.

## Design rules

1. Model cameras, microphones, locks, and occupancy data as sensitive assets.
2. Make security status and update support visible to buyers.
3. Log high-impact actions and provide recovery procedures.
4. Do not treat vendor claims as independent assurance; check certification, support, and incident history.

## Sources

- [NIST: Safer and more private smart homes](https://www.nist.gov/blogs/taking-measure/7-tips-keep-your-smart-home-safer-and-more-private-nist-cybersecurity)
- [European Commission: Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
- [FTC: Securing internet-connected devices](https://consumer.ftc.gov/articles/securing-your-internet-connected-devices-home)
