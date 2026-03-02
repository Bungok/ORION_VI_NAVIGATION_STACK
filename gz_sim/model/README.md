URDF generate:
```
xacro rover_model.xacro -o rover_model.urdf
```
Gazebo simulation run:
```
gz sim mars_yard.world 
```
or:
```
gz sim rover_model.urdf
```