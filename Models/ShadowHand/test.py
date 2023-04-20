import pybullet as p
import pybullet_data

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #used by loadURDF
p.setGravity(0,0,-10)
# planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
# boxId = p.loadURDF('shadowhand_gym/envs/assets/urdf/shadow_hand.urdf',cubeStartPos, cubeStartOrientation)
boxId = p.loadURDF('shadowhand_gym/envs/assets/obj/hammer.obj')

for i in range(10000):
    p.stepSimulation()
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()