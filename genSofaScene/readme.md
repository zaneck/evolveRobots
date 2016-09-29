# SofaScene Creator for evolveRobots
### Convert a Json File into a Sofa pyscn
Auteur: Valentin Owczarek


### How to:
- all usable sofa object are in sofaObjectUsable.py, you can expand it.
- all classes in sofaObject.py must not be use in your Json file.
- There are 2 kind of objects
   * unique one: Only One per Scene (PartialFixedConstraint...)
   * not unique one: multiple object with different values (ConstantForceField, FixedConstraint...)

- Json syntax:
  * JsonFile = {|OBJECT|+}
  * OBJECT = "ObjectName": UOBJECT || NUOBJECT
  * UOBJECT = {VARS}
  * NUOBJECT = [|{VARS},|* {VARS}]
  * VARS = |"ValueName":Value,|* "ValueName":Value

(With: || = or, + = One times or more, * zero time or more, |..| = motif separator)

- your json object must have at least:
   * a Canvas object with (divx, divY, divZ) the number of subdivision of the grid and x, y, z the canvas size in real world.

### Available Object
* Canvas
* PartialFixedConstraint
* FixedConstraint
* ConstantForceField


### How to run:
> python3 makeScene.py file.json expName

Create a folder name "expName" with all you need to run your Sofa simulation


# TO DO:
   - [x] Create main SofaObject to generate simple SofaScene
   - [ ] Create the organisor class
   - [ ] Create the write classes (pyscn, minTopo, controller)