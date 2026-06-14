# Level Up: Python – Challenge Solutions 🐍

This repository contains my personal solutions to the coding challenges featured in the [LinkedIn Learning](https://www.linkedin.com/learning/level-up-python) course **Level Up: Python** by [Barron Stone](https://linkedin.com)
The original course provides a series of standalone programming problems designed to stretch algorithmic thinking and reinforce core language mechanics. Every challenge in this repository has been successfully implemented and tested using the Python Standard Library.

---

## 🛠️ Tech Stack & Methodology
* **Language:** Python 3.x
* **Environment:** Developed and executed seamlessly via [GitHub Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces).
* **Philosophy:** High efficiency, low footprint. Adhering to the course's baseline, the majority of these solutions achieve optimal performance in under 24 lines of clean, readable code.

---

## Completed Challenges
Below is the roadmap of the 15 mini-projects completed and documented within this repo:

**Find Prime Factors** – Efficient mathematical factorization.
**Identify a Palindrome** – String manipulation and sequence checking.
**Sort a String** – Custom sorting logic over textual data.
**Find All List Items** – Target tracking and index extraction within collections.
**Play the Waiting Game** – Time-delayed execution and user interaction.
**Save a Dictionary** – Data serialization and structured file output.
**Schedule a Function** – Basic event loops and execution timing.
**Send an Email** – Leveraging Python network protocols for communication.
**Simulate Dice** – Randomization, statistics, and probability modeling.
**Count Unique Words** – Text parsing, cleaning, and frequency mapping.
**Generate a Password** – Cryptographically secure randomized string assembly.
**Merge CSV Files** – Flat-file I/O handling and data consolidation.
**Solve a Sudoku** – Implementing algorithmic backtracking / heuristics to solve matrix puzzles.
**Build a Zip Archive** – File compression and directory structuring.
**Download Sequential Files** – Network streams and sequential asset fetching.

---

## The Cybersecurity Edge
While these tasks focus on standard library fundamentals, my approach to writing code is heavily influenced by a **cybersecurity-first mindset**. Writing small, self-contained scripts is core to security automation, rapid tool building, and offensive/defensive operations.

* **Secure Coding Principles:** Solutions avoid unsafe evaluation sinks (like `eval()`), implement robust boundary testing, and use type assertions to eliminate structural vulnerabilities.
* **Scripting for Automation:** Challenges like parsing CSVs, scanning text metrics (word counting), and managing archive assets mirror tasks vital to security operations, such as log parsing, artifact carving, and automated malware staging.
* **Securing Assets:** The password generator module applies strict entropy requirements to verify password strength, shifting a simple puzzle into a production-minded security utility.

---

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed locally, or run the project in a cloud sandbox.

### Running Locally
1. Clone this repository to your machine:
   ```bash
   git clone https://github.com/BikDHINDSA/level-up-python
   cd level-up-python
   ```
2. Launch the master execution dashboard:
   ```bash
   python main.py
   ```
3. Alternatively, you can run individual scripts directly from the module folder:
   ```bash
   python challenges/solve_sudoku.py
   ```

### Running via GitHub Codespaces
1. Click the green **Code** button at the top right of this repository.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once your environment boots up, open your terminal and simply run:
   ```bash
   python main.py
   ```
