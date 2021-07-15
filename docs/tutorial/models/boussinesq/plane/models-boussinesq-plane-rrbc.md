back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---
The model equations are
```math
\begin{aligned}
\left(\partial_t - \Delta\right)\bold{u} &=  \bold{u}\times\left(\nabla\times\bold{u}\right) + \frac{Ra}{Pr}\Theta\bold{\hat{z}}  - \frac{1}{E}\hat{\bold{z}}\times\bold{u} - \nabla\Pi\\\\
\left(\partial_t - \frac{1}{Pr}\Delta\right)\Theta & = - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} & =0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
E & = \frac{\nu}{2\Omega d^2}\\\\
Pr &= \frac{\nu}{\kappa}\\\\
Ra &= \frac{g\alpha\beta d^4}{\nu\kappa}
\end{aligned}
```

The system is solved using a Toroidal/Poloidal decomposition of the velocity $`\bold{u}`$:
```math
\bold{u} = \nabla\times T\bold{\hat{z}} + \nabla\times\nabla\times P\bold{\hat{z}} + \chi(z)\bold{\hat{x}} + \gamma(z)\bold{\hat{y}}
```
and an anisotropic rescaling:
```math
\begin{aligned}
\tilde{\nabla}^2 & \equiv \nabla_h^2 + Ro^2\partial_z^2\\\\
\tilde{\nabla}^4 & \equiv \nabla_h^4 + 2 Ro^2\nabla_h^2\partial_z^2 + Ro^4\partial_z^4\\\\
\partial_{\tilde{z}} & \equiv Ro \partial_z\\\\
\tilde{Ra} & \equiv Ra E^{4/3}\\\\
Ro & \equiv E^{1/3}
\end{aligned}
```

The toroidal/poloidal equations become
```math
\begin{aligned}
N_\bold{u}& \equiv \left(\bold{\nabla}\times\bold{u}\right)\times\bold{u} \\\\
\partial_t\nabla^2_h T + \left(-\bold{\nabla}\times N_\bold{u}\right)_z & = \tilde{\nabla}^2\nabla_h^2 T + \frac{1}{Ro}\partial_{\tilde{z}}\nabla_h^2 P\\\\
\partial_t\tilde{\nabla}^2\nabla_h^2 P + \left(\bold{\nabla}\times\bold{\nabla}\times N_\bold{u}\right) & = \tilde{\nabla}^4\nabla_h^2 P - \frac{1}{Ro}\partial_{\tilde{z}}\nabla_h^2 T - \frac{\tilde{Ra}}{Pr}\nabla_h^2\theta\\\\
\partial_t\theta + N_\theta & = \frac{1}{Pr}\tilde{\nabla}^2\theta\\\\
\partial_t\chi + \overline{\left(N_{\bold{u}}\right)_x} & = \tilde{\nabla}^2\chi + \frac{1}{Ro}\gamma\\\\
\partial_t\gamma + \overline{\left(N_{\bold{u}}\right)_y} & = \tilde{\nabla}^2\gamma - \frac{1}{Ro}\chi\\\\
\partial\bar{\theta} + \overline{N_\theta} & = \frac{1}{Pr}\tilde{\nabla}^2\bar{\theta}
\end{aligned}
```
and
```math
T = 1 - z + \bar{\theta} + Ro \theta = 1 - z + Ro \overline{\overline{\theta}} + Ro\theta
```

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
