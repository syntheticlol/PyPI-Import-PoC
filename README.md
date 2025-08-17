# Import Exec Demo

This repository contains a **proof-of-concept (PoC)** Python package that demonstrates how importing a module can be abused to trigger code execution.

⚠️ **Disclaimer**:  
This project is for **educational and security research purposes only**.  
It does **not** contain harmful code.  
Do not use the techniques shown here for malicious purposes.

---

##  Background

- In older versions of Python packaging, there were `preinstall` and `postinstall` hooks that could be used to run code during installation.
- These were removed in newer versions for **security reasons**, since attackers abused them for supply chain attacks.
- While those hooks are gone, import-time execution is still possible using normal Python mechanisms (e.g., `__init__.py` or function wrappers).

This project demonstrates the *concept* safely so developers understand the risk.

---

##  Example (Safe Demonstration)

```python
import colorlib21

print(colorlib21.red("Hello, World!"))
```

Below is an example screenshot of how it appears in use:

![Example usage demonstrating color output](example.png)

In this demo, the `red()` function only prints colored text. In a real malicious scenario, importing the module or calling its functions could also trigger hidden actions.

---

##  Why this matters

- Software supply chain attacks are increasingly common.
- Attackers may abuse package names (typosquatting) or import-time behavior to trick developers.
- Developers should carefully vet dependencies before installing from PyPI.

---

##  References

- [PyPI Security Documentation](https://pypi.org/security/)  
- [OWASP Dependency Confusion Guide](https://owasp.org/www-community/attacks/Dependency_Confusion)  
- [Supply-Chain Attack Examples](https://snyk.io/blog/malicious-packages/)  

---

##  Responsible Use

This repository is a **PoC only**. It should not be used to create or distribute actual malware.  
If you discover vulnerabilities in Python packaging or PyPI, report them responsibly to the [PyPI Security Team](https://pypi.org/security/).
