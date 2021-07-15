back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---

The model equations are

streamfunction : 
```math
d_t \nabla^2_{\bot} \Psi + J[\Psi ,  \nabla^2_{\bot} \Psi]- \partial_Z W = \nabla^4_{\bot} \Psi
```
vertical velocity:
```math
d_t W + J[W, \nabla^2_{\bot} \Psi] + \partial_Z \Psi = \frac{\tilde{Ra}}{Pr} \theta + \nabla^2_{\bot} W
```
fluctuating temperature:
```math
d_t \theta + J[\theta, \nabla^2_{\bot} \Psi] +  W\partial_Z \overline{\Theta}  = \frac{1}{Pr} \nabla^2_{\bot} \theta
```
mean temperature:
```math
\partial_\tau \overline{\Theta}  +  \partial_Z\left ( \overline{W\theta}\right ) = \frac{1}{Pr} \partial_{ZZ}  \overline{\Theta}
```

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
