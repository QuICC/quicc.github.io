back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)

---

# Equations

The model equations are (see Sprague et al., 2006 for details)
```math
\begin{aligned}
\partial_t \zeta + J[\psi,\zeta] - \partial_Z w &= \nabla^2_\perp \zeta,\\
%
\partial_t w + J[\psi,w] + \partial_Z\psi &=\frac{\tilde{Ra}}{Pr} \theta + \nabla^2_\perp w,\\
%
\partial_t \theta + J[\psi,\theta] + w\partial_Z \overline{\Theta} &=\frac{1}{Pr}\nabla^2_\perp \theta,\\
%
\partial_Z(\overline{w\theta})&=\frac{1}{Pr}  (\partial_Z^2\overline{\Theta} + \mathcal{F}),
\end{aligned}
```
where:
```math
J[\psi,f] = \partial_x\psi \partial_y f-\partial_y\psi \partial_x f,
```
is the Jacobian; $\psi$ is the horizontal stream-function, defined as
```math
{\bf u}_\perp = (-\partial_y \psi,\partial_x\psi,0);
```
the axial voritcity is defined as
```math
\zeta = \partial_\perp^2\psi;
```
and $\mathcal{F}$ is the internal heating, function of $Z$.

Nondimensional parameters are:
```math
\tilde{Ra} = E^{4/3} Ra,
```
```math
E= \frac{\nu}{2\Omega H^2},
```
```math
Pr = \frac{\nu}{\kappa}.
```

# Implementation notes

## Numerics
The system is solved with a fourier decomposition in the horizontal and periodic $x$,$y$ directions and Chebyshev in the $Z$ direction.

## Nondimensionalisation

When the internal heating $\mathcal{F}$ is set to zero, the above set of equation reduces to the one with differential heating reported in, e.g., Sprague et al., 2006, and 
```math
Ra = \frac{g \alpha \Delta T H^3}{\nu \kappa}.
```

In the case of $\mathcal{F}\neq 0$ the Raylegih number definition needs to be adjusted. For uniform heat sources, $\mathcal{F}=1$ and $Ra$ is defined replacing $\Delta T$ with a temperature scale based on internal heating.

## Mean heat equation

The mean temperature $\overline{\Theta}$ is currently not solved for. What is of interested is its gradient $ \partial_Z\overline{\Theta}$. Because there is no time dependence in the mean temperature equation, we only need to deal with a "trivial" eqaution, integrated in the vertical direction:

```math
\partial_Z \overline{\Theta} = Pr (\overline{w\theta}) - \int \mathcal{F} dZ + c_0
```

where $\int \mathcal{F} dZ  $ is a primitive of $\mathcal{F}$ and $c_0$ is an integration constant.

In the original version of this model (e.g. Sprague et al., 2006) there is no internal heating and $c_0$ is chosen such that:
```math
-\partial_Z \overline{\Theta}|_{Z=Z_{top}}=-\partial_Z \overline{\Theta}|_{Z=Z_{bot}} = Nu = 1 + Pr \langle\overline{w\theta}\rangle,
```
resulting in:
```math
 \partial_Z \overline{\Theta} = Pr (\overline{w\theta} - \langle\overline{w\theta}\rangle) -1. \quad\text{(differential heating)}
```

Alternatively, $c_0$ could be picked so that 
```math
-\partial_Z \overline{\Theta}|_{Z=Z_{bot}}=0.
```

See description of the `bottom_dz_flux` parameter below for what is implemented.


# Parameters

## Physical

- `internal_heating`: 
    - `internal_heating = 0`: differential heating, $\mathcal{F}=0$
    - `internal_heating = 1`: internal heating with $\mathcal{F}=1$ 

- `bottom_dz_flux`: 
    - `bottom_dz_flux=-1` : flux adjusts to the dynamics. For the differential heating case, this makes the $\partial_Z \overline{\Theta}$ equation be:
        ```math
        \partial_Z \overline{\Theta} = Pr (\overline{w\theta} - \langle\overline{w\theta}\rangle) -1. \quad\text{(differential heating)}
        ```

    - `bottom_dz_flux=0` : zero flux at the bottom. For internal heating:
        ```math
        \partial_Z \overline{\Theta} = Pr (\overline{w\theta} - \int F dZ). \quad\text{(internal heating)},
        ```
        where the primitive $\int F dZ$ is zero at the bottom.






---

back to [home](home)/[models](models)/[boussinesq](models-boussinesq)/[plane](models-boussinesq-plane)
