back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---
The model equations are
```math
\begin{aligned}
\left(\partial_t - Pm\Delta\right)\bold{u} &=  \bold{u}\times\left(\bold{\nabla}\times\bold{u}\right) + \frac{Pm}{E}\left(\bold{\nabla}\times\bold{B}\right)\times\bold{B} + \frac{Pm^2Ra}{Pr}\Theta\bold{\hat{z}}  - \frac{Pm}{E}\hat{\bold{z}}\times\bold{u} - \nabla\Pi\\\\
\left(\partial_t - \Delta\right)\bold{B} &= \bold{\nabla}\times\left(\bold{u}\times\bold{B}\right)\\\\
\left(\partial_t - \frac{Pm}{Pr}\Delta\right)\Theta &= - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} &= 0\\\\
\nabla\cdot\bold{B} &= 0
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
E &= \frac{\nu}{2\Omega d^2}\\\\
Pr &= \frac{\nu}{\kappa}\\\\
Pm &= \frac{\nu}{\eta}\\\\
Ra &= \frac{g\alpha\beta d^4}{\nu\kappa}
\end{aligned}
```

The system is solved using a Toroidal/Poloidal decomposition of the velocity $`\bold{u}`$
```math
\bold{u} = \nabla\times T\bold{\hat{z}} + \nabla\times\nabla\times P\bold{\hat{z}} + \chi(z)\bold{\hat{x}} + \gamma(z)\bold{\hat{y}}
```
 and the magnetic field $`\bold{B}`$
```math
\bold{B} = \nabla\times \mathcal{T}\bold{\hat{z}} + \nabla\times\nabla\times \mathcal{P}\bold{\hat{z}} + \xi(z)\bold{\hat{x}} + \rho(z)\bold{\hat{y}}
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

The toroidal/poloidal equations for the velocity $`\bold{u}`$ become
```math
\begin{aligned}
N_\bold{u}& \equiv \left(\bold{\nabla}\times\bold{u}\right)\times\bold{u} + \frac{Pm}{E}\bold{B}\times\left(\bold{\nabla}\times\bold{B}\right)\\\\
\partial_t\nabla^2_h T + \left(-\bold{\nabla}\times N_\bold{u}\right)_z & = Pm\tilde{\nabla}^2\nabla_h^2 T + \frac{Pm}{Ro}\partial_{\tilde{z}}\nabla_h^2 P\\\\
\partial_t\tilde{\nabla}^2\nabla_h^2 P + \left(\bold{\nabla}\times\bold{\nabla}\times N_\bold{u}\right)_z & = Pm\tilde{\nabla}^4\nabla_h^2 P - \frac{Pm}{Ro}\partial_{\tilde{z}}\nabla_h^2 T - \frac{Pm^2\tilde{Ra}}{Pr}\nabla_h^2\theta\\\\
\partial_t\chi + \overline{\left(N_{\bold{u}}\right)_x} & = Pm\tilde{\nabla}^2\chi + \frac{Pm}{Ro}\gamma\\\\
\partial_t\gamma + \overline{\left(N_{\bold{u}}\right)_y} & = Pm\tilde{\nabla}^2\gamma - \frac{Pm}{Ro}\chi
\end{aligned}
```
and the equations for the magnetic field $`\bold{B}`$ become
```math
\begin{aligned}
\partial_t\nabla^2_h \mathcal{P} + \left(-\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right)\right)_z & = \tilde{\nabla}^2\nabla_h^2 \mathcal{P}\\\\
\partial_t\nabla_h^2 \mathcal{T} + \left(-\bold{\nabla}\times\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right) \right)_z & = \tilde{\nabla}^2\nabla_h^2 \mathcal{T}\\\\
\partial_t\xi + \overline{\left(\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right)\right)_x} & = \tilde{\nabla}^2\xi \\\\
\partial_t\rho + \overline{\left(\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right)\right)_y} & = \tilde{\nabla}^2\rho
\end{aligned}
```
and for the temperature $`\Theta`$
```math
\begin{aligned}
\partial_t\theta + N_\theta & = \frac{Pm}{Pr}\tilde{\nabla}^2\theta\\\\
\partial\bar{\theta} + \overline{N_\theta} & = \frac{Pm}{Pr}\tilde{\nabla}^2\bar{\theta}
\end{aligned}
```
and
```math
T = 1 - z + \bar{\theta} + Ro \theta = 1 - z + Ro \overline{\overline{\theta}} + Ro\theta
```

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
