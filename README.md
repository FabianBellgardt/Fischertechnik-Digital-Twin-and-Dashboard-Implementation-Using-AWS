# AWS-Based Digital Twin and Dashboard for Fischertechnik Factory
<img width="2740" height="2664" alt="diagram_gesamt" src="https://github.com/user-attachments/assets/f1328259-929c-488a-a7c6-d58f08da9d36" />
This repository contains the core files for implementing a cloud-based control system and a digital twin of the Fischertechnik model factory on Amazon Web Services (AWS).  
It includes Node-RED dashboards, configuration files, a simplified 3D factory model, and Python code for AWS Lambda. This repository was created as part of a Master's thesis.  
The goal is to migrate the factory control and visualization from the proprietary manufacturer cloud to AWS, enabling vendor-independent operations and providing added value through flexible extensions such as a digital twin and Grafana dashboards.


## Repository Contents

### Node-RED_Dashboard_for_EC2.json
This JSON file contains the entire code for the Node-RED instance running on the EC2 instance on AWS. It can be used to visualize the status of the factory and control it.

### Node-RED_factory_raspberrypi.json
This file contains the complete JSON code that runs on the Raspberry Pi. Several tabs have been created that connect to AWS IoT Core. Specifically, to two IoT things:

  -  fischertechnik_thing
  -  fischertechnik_thing_iso

  This file enables the forwarding of MQTT messages to AWS and the reception of MQTT messages from AWS.

### Step-by-Step Guide: AWS-based digital twin  
A detailed guide for setting up an AWS-based control dashboard and digital twin.  
Provides step-by-step instructions to reproduce the control dashboard and the digital twin.

### factory_modell_elements_named.glb
Manually created and simplified a 3D CAD model of the factory in GLB format.  
Used in AWS IoT TwinMaker for visualization.

  <img width="1134" height="765" alt="picture_factory_CAD_fabian" src="https://github.com/user-attachments/assets/201013e8-f7e9-4a32-9a41-0f741ca9da6d" />


### lambda_python_code.py
Python code for an AWS Lambda function.  
Processes MQTT messages, extract relevant data, and stores it in AWS SiteWise.

### VIDEO_digitaltwin_bellgardt.mp4
This video shows the core features of the digital twin developed in this thesis.

## The AWS-Based Control Dashboard
<img width="1946" height="1231" alt="dashboard_all" src="https://github.com/user-attachments/assets/6c235f78-6baa-45ba-8aec-5ca6de25008b" />


## The AWS-Based Digital Twin

### Highlighting Active Factory Parts
<img width="1373" height="970" alt="digtwin_active_factory_parts" src="https://github.com/user-attachments/assets/88b62d55-39ba-40bd-aed1-f7685cee214a" />

### Visualize Fillstate of the High-Bay-Warehouse
<img width="1395" height="1299" alt="factory_hbw" src="https://github.com/user-attachments/assets/effd01fb-5504-4f91-bba1-78813d117879" />

<img width="1405" height="1011" alt="digtwin_hbw_fill" src="https://github.com/user-attachments/assets/b9cf8740-9000-4536-97fd-495e2631928f" />

### Additional Managed Grafana Widgets
<img width="2096" height="1389" alt="digtwin_screenshot_grafana" src="https://github.com/user-attachments/assets/b74d1ae8-441a-4621-a347-b6ab1d3fecc1" />

### Information Windows in 3D Environment
<img width="1308" height="1031" alt="digtwin_panels" src="https://github.com/user-attachments/assets/c8286251-f36b-419f-8284-d1481c2fef50" />





  
