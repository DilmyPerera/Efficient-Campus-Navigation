# **Efficient Campus Navigation**

## **A Shortest Path Finding System for the University of Vavuniya**

---

## **Introduction**

Navigating the University of Vavuniya campus can be challenging due to its complex layout. To address this issue, we have developed an efficient campus navigation system. This system aims to provide students, staff, and visitors with the shortest and most efficient paths between any two locations on campus.

## **Purpose**

The primary objective of this project is to enhance campus navigation, ensuring safety and efficiency. By implementing a pathfinding system based on Dijkstra's Algorithm, the project aims to:

- Improve day-to-day navigation for students and staff.
- Enhance emergency response times.
- Facilitate better event management.
- Ensure accessibility for all individuals.
- Reduce environmental impact and psychological stress associated with navigation.

---

## **Features**

- **Interactive Map Interface**: A user-friendly, interactive map to help users visualize and navigate the campus.
- **Path Calculation** : Computes the shortest path between two locations
- **Emergency Routing**: Specialized routing to assist in quick emergency response.
- **Scalability** : Designed to accommodate future campus expansions and data integrations.

---

## **Technology Stack**

- Programming Language: **Python**
- Algorithms: **Dijkstra's Algorithm** for shortest path calculation
- Libraries :
  - **Tkinter** for GUI
  - **PIL** **(Pillow)** for image processing
  - **heapq** for priority queue operations
  - **math** for calculations
  - **ImageTk** for handling images in Tkinter

---

## **Step-by-Step Guide to Run Navigation System**

#### Prerequisites

- Download Python [here](https://www.python.org/downloads/)
- An IDE
  - Visual Studio Code [here](https://code.visualstudio.com/download)
  - Pycharm [here](https://www.jetbrains.com/pycharm/download/)

#### Installation

- Clone the repository:

```
https://github.com/DilmyPerera/Efficient-Campus-Navigation.git
```

- Navigate to the project Directory:

```
cd Efficient-Campus-Navigation
```

- Install Required Dependencies
  - Note: some libraries might be installed with the IDE, if not import them using below commands

```
pip install tkinter

pip install PIL (PIL or Pillow)

pip install heapq
```

- Execute the Python Program using the IDE
```
python campus_navigation.py
```
  
- Using the Application
  - Enter the Source Point in the provided input field.
  - Enter the Destination Point in the provided input field.
  - Click the Find Shortest Path button.
  - The application will display the shortest path on the map with a red line, and the points will be shown in chronological order. The calculated distance will also be displayed.
---

## Graphical User Interface

![GUI](https://github.com/DilmyPerera/Efficient-Campus-Navigation/assets/113934417/7e831112-712f-49bd-93cb-cf1462a44394)

**After Execution**

![Gui After](https://github.com/DilmyPerera/Efficient-Campus-Navigation/assets/113934417/dd64f7c0-ff72-40cb-9757-ad9d00d68b5e)



## **Conclusion**

The Efficient Campus Navigation system for the University of Vavuniya provides a significant improvement in navigating the campus. By combining traditional pathfinding algorithms , this system offers reliable and adaptive navigation solutions. It enhances the campus experience by making navigation more intuitive, efficient, and responsive to real-time conditions. Future enhancements could include expanded datasets, additional machine learning models, and further integration with campus infrastructure

For more Details view Project Report [here](https://github.com/user-attachments/files/15905066/Report.pdf)
