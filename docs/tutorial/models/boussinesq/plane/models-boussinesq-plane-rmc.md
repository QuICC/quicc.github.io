back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---
The model equations are
```math
\begin{aligned}
\left(\partial_t - Pm\Delta\right)\bold{u} &=  \bold{u}\times\left(\bold{\nabla}\times\bold{u}\right) + Q Pm\left(\bold{\nabla}\times\bold{B}\right)\times\bold{B} - \frac{Pm}{E}\hat{\bold{z}}\times\bold{u} + \frac{Pm^2Ra}{Pr}\Theta\bold{\hat{z}} - \nabla\Pi\\\\
\left(\partial_t - \Delta\right)\bold{B} &= \bold{\nabla}\times\left(\bold{u}\times\bold{B}\right)\\\\
\left(\partial_t - \frac{Pm}{Pr}\Delta\right)\Theta &= - \bold{u}\cdot\nabla\Theta\\\\
\nabla\cdot\bold{u} &= 0\\\\
\nabla\cdot\bold{B} &= 0\\\\
\bold{B} &=  \bold{B}_0 + \bold{b}
\end{aligned}
```

with the parameters defined as
```math
\begin{aligned}
E &= \frac{\nu}{2\Omega d^2}\\\\
Pr &= \frac{\nu}{\kappa}\\\\
Pm &= \frac{\nu}{\eta}\\\\
Ra &= \frac{g\alpha\beta d^4}{\nu\kappa}\\\\
Q &= \frac{B_0^2 d^2}{\mu_0\rho\nu\eta}
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

The toroidal/poloidal equations for the velocity $`\bold{u}`$ become
```math
\begin{aligned}
\partial_t\nabla^2_h T + \left(-\bold{\nabla}\times N_\bold{u}\right)_z & = Pm\nabla^2\nabla_h^2 T + \frac{Pm}{E}\partial_z\nabla_h^2 P\\\\
\partial_t\nabla^2\nabla_h^2 P + \left(\bold{\nabla}\times\bold{\nabla}\times N_\bold{u}\right)_z & = Pm\nabla^4\nabla_h^2 P - \frac{Pm}{E}\partial_z\nabla_h^2 T - \frac{Pm^2 Ra}{Pr}\nabla_h^2\theta\\\\
\partial_t\chi + \overline{\left(N_{\bold{u}}\right)_x} & = Pm\nabla^2\chi + \frac{Pm}{Ro}\gamma\\\\
\partial_t\gamma + \overline{\left(N_{\bold{u}}\right)_y} & = Pm\nabla^2\gamma - \frac{Pm}{Ro}\chi
\end{aligned}
```
and the equations for the magnetic field $`\bold{B}`$ become
```math
\begin{aligned}
\partial_t\nabla^2_h \mathcal{P} + \left(-\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right)\right)_z & = \nabla^2\nabla_h^2 \mathcal{P}\\\\
\partial_t\nabla_h^2 \mathcal{T} + \left(-\bold{\nabla}\times\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right) \right)_z & = \nabla^2\nabla_h^2 \mathcal{T}\\\\
\partial_t\xi + \overline{\left(\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right)\right)_x} & = \nabla^2\xi \\\\
\partial_t\rho + \overline{\left(\bold{\nabla}\times\left(\bold{B}\times\bold{u}\right)\right)_y} & = \nabla^2\rho
\end{aligned}
```

---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
