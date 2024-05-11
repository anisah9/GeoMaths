# GeoMaths

GeoMaths is an interactive educational tool designed to help Year 6 students learn and understand geometry through coding activities and visual demonstrations. This tool supports the drawing and manipulation of 2D shapes and allows for the real-time visualization of geometric transformations.

## Features

- **Shape Manipulation**: Draw and manipulate basic and complex 2D shapes including squares, circles, rectangles, triangles, and polygons.
- **Advanced Geometry Concepts**: Learn transformations such as translations and reflections.
- **Real-Time Visualization**: Execute Python code to visualize geometric concepts dynamically on a canvas.
- **Coding Activities**: Create custom shapes and patterns through a user-friendly coding interface.
- **User Interface**: Intuitive and accessible interface with age-appropriate interactive elements, including a code editor and visual output canvas.
- **Saving and Exporting**: Save your work and export drawings as images in various formats like PNG and JPEG.
- **Random Challenges**: Engage with randomly generated geometry challenges to foster problem-solving skills.
- **Tutorials**: Tutorials explain complex geometry concepts in an understandable manner.

## Installation and Execution Instructions

Follow these detailed steps to set up and run the GeoMaths application:

### Environment Setup

- Install Python 3.8 or newer. Download from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your OS.
- Ensure Python and pip (Python's package installer) are added to your system's PATH.

### Install Dependencies

- Open a terminal or command prompt.
- Install required Python libraries using pip:
  ```bash
  pip install tk matplotlib pillow
  ```

### Clone the Repository

- Navigate to the location where you want the project files on your system.
- Run the following command to clone the repository:
  ```bash
  git clone https://github.com/anisah9/GeoMaths.git
  ```

### Change into the Project Directory

- Change directory into the project:
  ```bash
  cd GeoMaths
  ```

### Install Dependencies

For macOS:

1. Open the Terminal.
2. Navigate to your project directory.

```bash
cd path/to/GeoMaths
```

3. Create the virtual enviroment:

```bash
python3 -m venv myenv
```

4. Activate the virtual environment:

```bash
source myenv/bin/activate
```

5. To deactivate:

```bash
deactivate
```

For Windows:

1. Open the Terminal.
2. Navigate to your project directory.

```bash
cd path/to/GeoMaths
```

3. Create the virtual enviroment:

```bash
py -m venv myenv
```

4. Activate the virtual environment:

- Command Prompt:
  ```bash
  source myenv/bin/activate
  ```
- PowerShell:
  ```bash
  myenv\Scripts\Activate.ps1
  ```

5. To deactivate:

```bash
deactivate
```

### Run the Application

- Execute the main script using Python:
  ```bash
  python main.py
  ```

This will launch the GeoMaths GUI, where you can begin interacting with the application.
