# DAQ Suite — Intelligent DAQ Configuration, Simulation and Code Generation

Short description
This project simplifies configuring, generating code for, and simulating Data Acquisition (DAQ) systems. It provides an interactive GUI, live simulation and visualization, adaptive semantic validation, and automatic code generation for multiple DAQ platforms.

Highlights
- GUI (Tkinter) for interactive configuration and device selection
- Live simulation and visualization (time domain and FFT) using Matplotlib
- Configuration save/load in JSON format
- Automatic code generation for:
  - NI-DAQmx (C/C++)
  - Serial/COM (Python using pyserial)
- Standalone .exe built with PyInstaller for Windows (Python not required)
- Graceful degradation when NI-DAQmx is not available (Simulation-only / Serial mode)

Repository
https://github.com/Saidmurotov/dissertatsiya

Quick start
1. Install (development environment):
   - Python 3.11.9 (recommended for compatibility with nidaqmx and PyInstaller)
   - pip install -r requirements.txt

2. Run GUI:
   - python gui.py

3. Use the GUI to:
   - Detect connected devices (NI-DAQmx and serial ports)
   - Configure channels, sample rates, and acquisition parameters
   - Simulate acquisition and view live plots (time-domain and FFT)
   - Generate code for selected target (NI-DAQmx C/C++ or Python for microcontrollers)

Standalone executable
A released Windows executable (.exe) has been built using PyInstaller targeting Python 3.11.9 to avoid metadata/packaging issues with nidaqmx. See the Releases section of the repository for download.

Technical requirements
- Python >= 3.11.9
- Key dependencies (see requirements.txt):
  - numpy
  - matplotlib
  - pyserial
  - nidaqmx (optional; if not present, the app runs in Simulation/Serial mode)

Files of interest
- gui.py — main GUI, simulation and interaction logic
- daq_config.py — DAQ settings model and validation
- code_generator.py — code generation for NI-DAQmx and Serial targets
- device_inspector.py — device discovery (NI-DAQmx, COM ports)
- DAQ_Suite.spec — PyInstaller spec for building the executable
- requirements.txt, .gitignore

Known limitations & compatibility
- Built and tested with Python 3.11.9 due to compatibility constraints with nidaqmx and PyInstaller.
- If NI-DAQmx driver or python package is missing, NI features are disabled and the app will offer Simulation or Serial-only usage.

Future improvements
- Add support for LabJack and PyVISA backends
- Extend signal processing (digital filters, RMS, triggering)
- Add a Data Viewer tab for CSV analysis and a plugin architecture
- Improve diagnostics, suggestion messages, and traceability of validation decisions

License
Choose and include an appropriate license file (e.g., MIT) in the repository.

Contact / Contributions
See CONTRIBUTING.md for contribution guidelines. For questions, open an issue in the GitHub repository.