back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---
The model equations are
```math
\begin{aligned}
\left(\partial_t - \Delta\right)\bold{u} &=  \bold{u}\times\left(\nabla\times\bold{u}\right) + \frac{Ra}{Pr}\Theta\bold{\hat{z}} - \nabla\Pi\\\\
\left(\partial_t - \frac{1}{Pr}\Delta\right)\Theta & = - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} & =0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
Pr &= \frac{\nu}{\kappa}\\\\
Ra &= \frac{g\alpha\beta d^4}{\nu\kappa}
\end{aligned}
```

The system is solved using a Toroidal/Poloidal decomposition of the velocity $`\bold{u}`$:
```math
\bold{u} = \nabla\times T\bold{\hat{z}} + \nabla\times\nabla\times P\bold{\hat{z}} + \chi(z)\bold{\hat{x}} + \gamma(z)\bold{\hat{y}}
```

The toroidal/poloidal equations become
```math
\begin{aligned}
N_\bold{u}& \equiv \left(\bold{\nabla}\times\bold{u}\right)\times\bold{u}\\\\
\partial_t\nabla^2_h T + \left(-\bold{\nabla}\times N_\bold{u}\right)_z & = \nabla^2\nabla_h^2 T\\\\
\partial_t\nabla^2\nabla_h^2 P + \left(\bold{\nabla}\times\bold{\nabla}\times N_\bold{u}\right) & = \nabla^4\nabla_h^2 P - \frac{Ra}{Pr}\nabla_h^2\theta\\\\
\partial_t\theta + N_\theta & = \frac{1}{Pr}\nabla^2\theta\\\\
\partial_t\chi + \overline{\left(N_{\bold{u}}\right)_x} & = \nabla^2\chi \\\\
\partial_t\gamma + \overline{\left(N_{\bold{u}}\right)_y} & = \nabla^2\gamma \\\\
\partial\bar{\theta} + \overline{N_\theta} & = \frac{1}{Pr}\nabla^2\bar{\theta}
\end{aligned}
```
and
```math
T = 1 - z + \bar{\theta} + \theta
```

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
