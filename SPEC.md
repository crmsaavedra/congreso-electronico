# SPEC.md — Congreso Electrónico 2026 Landing Page

## 1. Concept & Vision

Una landing page de alto impacto para el Congreso Electrónico 2026 que combina estética tecnológica con animaciones fluidas. El diseño evoca circuitos impresos, microchips y la energía vibrante de la innovación electrónica. Cada sección es una "etapa" del recorrido tecnológico, con animaciones únicas que mantienen al visitante comprometido. La experiencia transmite profesionalismo académico con toques futuristas.

## 2. Design Language

### Aesthetic Direction
Estilo "Tech Noir Electrónico" — mezclando la oscuridad del navy (#0D1520) con destellos de azul eléctrico (#0050D6) y acentos dorados de microchips (#FFB81C). Circuitos sutiles decorativos, glassmorphism para cards, y efectos de brillo/glow para elementos interactivos.

### Color Palette
| Color | Hex | Uso |
|-------|-----|-----|
| Navy Oscuro | #0D1520 | Fondos principales, texto primario |
| Azul Vibrante | #0050D6 | Acentos, elementos destacados, CTAs |
| Amarillo Dorado | #FFB81C | Highlights, microchip, CTAs secondary |
| Blanco Puro | #FFFFFF | Fondo principal, texto sobre oscuro |
| Gris Tech | #1E2A3A | Cards, elementos secundarios |
| Azul Claro | #4A90D9 | Links, elementos desupport |

### Typography
- **Títulos**: Rajdhani (700) — fuente tech/futurista con carácter
- **Body**: Inter (400, 500) — legibilidad óptima
- **Acentos/Código**: JetBrains Mono — para detalles técnicos
- **Fallback**: system-ui, sans-serif

### Spatial System
- Base unit: 8px
- Sections: 120px padding vertical desktop, 80px móvil
- Cards: 24px padding, 16px gap entre cards
- Max-width content: 1200px

### Motion Philosophy
- **Entrada**: Fade-in + translateY (0→0, opacity 0→1), 600ms ease-out
- **Stagger**: 100ms delay entre elementos secuenciales
- **Hover**: Scale 1.02-1.05, 300ms ease, shadow glow
- **Parallax**: Factor 0.3-0.5 para profundidad sutil
- **Typing**: 80ms por caracter
- **Counter**: 2000ms de duración, easing exponencial

### Visual Assets
- **Iconos**: SVG custom representando circuitos, chips, ondas
- **Decoración**: Circuit board patterns como líneas sutiles de fondo
- **Imágenes**: Placeholder gradients con efecto glass
- **Particles**: Sistema de partículas conectadas estilo "circuito vivo"

## 3. Layout & Structure

### Page Flow (13 secciones)
1. **Hero** (100vh) — Video/Particles background, logo animado, typing title, countdown, CTA
2. **Sobre** — Stats con contadores, cards glassmorphism
3. **Programa** — Timeline visual con bloques de horarios
4. **Actividades** — Grid de 6 cards con animaciones flip/reveal
5. **Cronograma** — Tabla visual 3 días, tabs interactivos
6. **Speakers** — Cards con efecto stagger
7. **Técnicas** — Grid expandible de temáticas
8. **Workshops** — Cards apiladas con badges
9. **Precios** — Tabla comparativa con etapas de preventa
10. **Auspicios** — Badges metálicos animados
11. **Organizadores** — Logos con stats
12. **Voluntariado** — Card con CTA
13. **Footer** — Links, social, copyright

### Responsive Strategy
- Mobile-first approach
- Breakpoints: 320px, 480px, 768px, 1024px, 1440px
- Cards stack vertical en móvil
- Navigation → hamburger menu <768px
- Hero typography scales: clamp(2rem, 8vw, 5rem)

## 4. Features & Interactions

### Animations by Section

**Hero Section:**
- Partículas de circuito en canvas (60 partículas, líneas conectoras)
- Logo: scale 0→1 con bounce, 800ms
- Título: typing effect con cursor parpadeante
- Countdown: números con flip animation
- CTA: glow pulse animation continua

**Sobre el Congreso:**
- Stats: counter animation de 0 al valor final
- Cards: glassmorphism con parallax al hover

**Actividades (Cards más importantes):**
- Ponencias: 3D flip card (front: icono, back: descripción)
- Papers: documento flotante con efecto de levitación
- Talleres: iconos con magnetic hover effect
- Exhibición: lightbox gallery con zoom
- Networking: burbujas animadas estilo "bubble network"
- Cierre: confetti explosion al hover

**Timeline/Cronograma:**
- Scroll reveal staggered: cada bloque aparece 100ms después
- Active day indicator con slide animation

**Precios:**
- Tabla con hover que expande detalles
- Badge de ahorro con bounce animation
- CTAs con ripple effect al click

**Sponsorships:**
- Badges metálicos (gradient oro/plata/bronce)
- Shine effect horizontal al hover

### Scroll Interactions
- Header: transparente → sólido con blur al scroll
- Progress bar: indicador de posición en página
- Back to top: aparece después de 500px scroll, bounce animation

### Preloader
- Logo central con pulse animation
- Carga simulada con progress bar
- Fade out con scale up

## 5. Component Inventory

### Header/Navigation
- **Default**: transparente, logo + links
- **Scrolled**: blur background, shadow
- **Mobile**: hamburger → slide-in menu

### Buttons
- **Primary**: Azul (#0050D6), texto blanco, rounded
- **Secondary**: Outline amarillo (#FFB81C)
- **Glow**: Box-shadow pulsante
- **Hover**: scale(1.05), brighter
- **Active**: scale(0.98)

### Cards
- **Glass**: background rgba(255,255,255,0.05), blur(10px), border white/20
- **Hover**: translateY(-8px), shadow expansion
- **Content**: icono + título + descripción

### Countdown Units
- Números grandes (Rajdhani 700)
- Labels pequeños debajo
- Separadores ":" con blink animation

### Badges
- Pill shape, uppercase
- Colores según contexto (amarillo=urgent, azul=info)
- Pulse animation para "PRIMERA PREVENTA"

### Timeline Blocks
- Left border colored por día
- Time badge a la izquierda
- Content card a la derecha
- Connector lines verticales

### Tables
- Zebra striping con opacity
- Sticky header
- Row hover highlight

## 6. Technical Approach

### Stack
- HTML5 semántico
- CSS3 (custom properties, grid, flexbox)
- Vanilla JavaScript (ES6+)

### Architecture
- Single index.html file
- CSS inline en `<style>`
- JS inline en `<script>`
- No external dependencies excepto Google Fonts

### Key Implementations
```javascript
// Intersection Observer para scroll reveals
const observer = new IntersectionObserver(callback, {threshold: 0.1});

// Counter animation
function animateCounter(el, target, duration);

// Particle system
class Particle { update(), draw(), connect(); }

// Typing effect
function typeText(el, text, speed);
```

### Performance Considerations
- Particles limitadas a 60
- RequestAnimationFrame para animaciones
- Debounce en scroll handlers
- Lazy load para secciones below fold
- CSS transforms para GPU acceleration

## 7. Content Structure

### Hero
- Logo: "CE26" con chip icon
- Title: "CONGRESO ELECTRÓNICO 2026"
- Subtitle: "Innovación, Tecnología y Electrónica"
- Dates: "11, 12 y 13 de noviembre"
- Location: "Universidad de Concepción, Chile"
- Badge: "PRIMERA PREVENTA"
- CTA: "¡Inscíbete Ahora!"

### About Stats
- "+200 Asistentes esperados"
- "+75 Estudiantes IEEE RAS activos"
- "3 Días de evento"
- "8+ Charlas técnicas"

### Activities (6 items)
1. Ponencias y Charlas
2. Llamado a Papers
3. Talleres Prácticos
4. Exhibición Tecnológica
5. Coffee Breaks & Networking
6. Celebración de Cierre

### Pricing Tiers
| Categoría | Preventa 1 | Preventa 2-3 | Venta |
|-----------|------------|--------------|-------|
| Concursante Paper | $12.000 | $15.000 | $20.000 |
| IEEE Miembro | $7.000 | $10.000 | $15.000 |
| Mechón UdeC | $8.000 | $12.000 | $16.000 |
| Estudiante UdeC | $10.000 | $15.000 | $20.000 |
| Estudiante Otra | $12.000 | $17.000 | $22.000 |
| Profesional | $15.000 | $22.000 | $30.000 |

### Sponsorships
- Platino: $500.000
- Oro: $300.000
- Plata: $150.000
- Bronce: $75.000
- Apoyo: $30.000

### Organizers
- IEEE RAS UdeC: +75 miembros, Biobío AI_Robotics Summit
- Centro Estudiantes ICE: años de experiencia