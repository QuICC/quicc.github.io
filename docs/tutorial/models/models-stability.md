back to [home](/)/[tutorial](/tutorial)/[models](/tutorial/tutorial-models)

---

Physical models can have three levels of stability:
- **Devel:** At this stage, the model is still under development. It doesn't necessary compile. It could also simply be a test of a new approach that might not be completed.
- **Staging:** At this stage, the model compiles and runs successfully. It has not yet been fully tested and benchmarked and results need to be considered carefully.
- **Stable:** At this stage, the model compiles and runs successfully. A complete test and benchmark suite is also available and the implementation has been validated against it.

The stability of the a physical model is defined by where it's stored in the source code tree. The repository structure looks like:
```
Model/Devel/Boussinesq/Plane/Model1/:
                                   PhysicalModel.hpp
                                   EquationA.hpp
                                   EquationB.hpp
Model/Staging/Boussinesq/Shell/Model2/:
                                   PhysicalModel.hpp
                                   EquationA.hpp
                                   EquationB.hpp
                                   EquationC.hpp
Model/Stable/Boussinesq/Sphere/Model3/:
                                   PhysicalModel.hpp
                                   EquationA.hpp
```

---

back to [home](/)/[tutorial](/tutorial)/[models](/tutorial/tutorial-models)
