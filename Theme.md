# Frontend Theme Documentation

## Overview
This document outlines the complete theme system used for frontend design and animations in the AI Interview Neuro Sync application.

## Design System

### Color Palette

#### Custom Colors (Defined in Tailwind Config)
```css
--color-green: #b9ff66;  /* Primary accent color */
--color-gray: #f3f3f3;   /* Light gray background */
--color-dark: #191a23;   /* Dark text/background */
```

#### Light Theme (Default)
All colors use OKLCH color space for better accessibility and theming:

```css
--background: oklch(1 0 0);                    /* Pure white */
--foreground: oklch(0.145 0 0);               /* Near black text */
--card: oklch(1 0 0);                         /* White cards */
--card-foreground: oklch(0.145 0 0);          /* Card text */
--popover: oklch(1 0 0);                      /* Popover background */
--popover-foreground: oklch(0.145 0 0);       /* Popover text */
--primary: oklch(0.205 0 0);                  /* Primary buttons */
--primary-foreground: oklch(0.985 0 0);       /* Primary text */
--secondary: oklch(0.97 0 0);                 /* Secondary elements */
--secondary-foreground: oklch(0.205 0 0);     /* Secondary text */
--muted: oklch(0.97 0 0);                     /* Muted backgrounds */
--muted-foreground: oklch(0.556 0 0);         /* Muted text */
--accent: oklch(0.97 0 0);                    /* Accent elements */
--accent-foreground: oklch(0.205 0 0);        /* Accent text */
--destructive: oklch(0.577 0.245 27.325);     /* Error/danger */
--border: oklch(0.922 0 0);                   /* Border colors */
--input: oklch(0.922 0 0);                    /* Input fields */
--ring: oklch(0.708 0 0);                     /* Focus rings */
```

#### Dark Theme
```css
--background: oklch(0.145 0 0);               /* Dark background */
--foreground: oklch(0.985 0 0);               /* Light text */
--card: oklch(0.205 0 0);                     /* Dark cards */
--card-foreground: oklch(0.985 0 0);          /* Card text */
--popover: oklch(0.205 0 0);                  /* Dark popover */
--popover-foreground: oklch(0.985 0 0);       /* Popover text */
--primary: oklch(0.922 0 0);                  /* Light primary */
--primary-foreground: oklch(0.205 0 0);       /* Dark primary text */
--secondary: oklch(0.269 0 0);                /* Dark secondary */
--secondary-foreground: oklch(0.985 0 0);     /* Light secondary text */
--muted: oklch(0.269 0 0);                    /* Dark muted */
--muted-foreground: oklch(0.708 0 0);         /* Muted text */
--accent: oklch(0.269 0 0);                   /* Dark accent */
--accent-foreground: oklch(0.985 0 0);        /* Light accent text */
--destructive: oklch(0.704 0.191 22.216);     /* Dark danger */
--border: oklch(1 0 0 / 10%);                 /* Semi-transparent borders */
--input: oklch(1 0 0 / 15%);                  /* Semi-transparent inputs */
--ring: oklch(0.556 0 0);                     /* Dark focus rings */
```

#### Chart Colors
```css
--chart-1: oklch(0.646 0.222 41.116);         /* Warm orange */
--chart-2: oklch(0.6 0.118 184.704);          /* Blue */
--chart-3: oklch(0.398 0.07 227.392);         /* Dark blue */
--chart-4: oklch(0.828 0.189 84.429);         /* Yellow-green */
--chart-5: oklch(0.769 0.188 70.08);          /* Orange */

/* Alternative hex values for charts */
--chart-1: #2D3748;                           /* Dark gray */
--chart-2: #4A5568;                           /* Medium gray */
--chart-3: #2D3748;                           /* Same as chart-2 */
--chart-4: #718096;                           /* Light gray */
--chart-5: #E2E8F0;                           /* Very light gray */
```

#### Sidebar Theme
```css
--sidebar: oklch(0.985 0 0);                  /* Light sidebar */
--sidebar-foreground: oklch(0.145 0 0);       /* Sidebar text */
--sidebar-primary: oklch(0.205 0 0);          /* Sidebar primary */
--sidebar-primary-foreground: oklch(0.985 0 0); /* Sidebar primary text */
--sidebar-accent: oklch(0.97 0 0);            /* Sidebar accent */
--sidebar-accent-foreground: oklch(0.205 0 0); /* Sidebar accent text */
--sidebar-border: oklch(0.922 0 0);           /* Sidebar borders */
--sidebar-ring: oklch(0.708 0 0);             /* Sidebar focus rings */

/* Dark sidebar variants */
--sidebar-foreground: oklch(0.985 0 0);       /* Light text */
--sidebar-primary: oklch(0.488 0.243 264.376); /* Purple primary */
--sidebar-primary-foreground: oklch(0.985 0 0); /* Light text */
--sidebar-accent: oklch(0.269 0 0);           /* Dark accent */
--sidebar-accent-foreground: oklch(0.985 0 0); /* Light text */
--sidebar-border: oklch(1 0 0 / 10%);         /* Transparent border */
--sidebar-ring: oklch(0.556 0 0);             /* Dark ring */
```

## Typography

### Fonts
```css
--font-sans: var(--font-geist-sans);          /* Main sans-serif font */
--font-mono: var(--font-geist-mono);          /* Monospace font for code */
```

### Border Radius
```css
--radius: 0.625rem;                           /* Base radius: 10px */
--radius-sm: calc(var(--radius) - 4px);       /* Small radius: 6px */
--radius-md: calc(var(--radius) - 2px);       /* Medium radius: 8px */
--radius-lg: var(--radius);                   /* Large radius: 10px */
--radius-xl: calc(var(--radius) + 4px);       /* Extra large radius: 14px */
```

## Animations

### Ripple Animation
Two-layer ripple effect for interactive elements:

```css
@keyframes ripple1 {
  0% { transform: scale(1); opacity: 0.7; }
  100% { transform: scale(4); opacity: 0; }
}

@keyframes ripple2 {
  0% { transform: scale(1); opacity: 0.5; }
  100% { transform: scale(3); opacity: 0; }
}

.animate-ripple1 { animation: ripple1 2s infinite ease-out; }
.animate-ripple2 { 
  animation: ripple2 2s infinite ease-out; 
  animation-delay: 0.5s; 
}
```

### Blob Animation
Organic floating animation for decorative elements:

```css
@keyframes blob {
  0% { transform: translate(0px, 0px) scale(1); }
  33% { transform: translate(30px, -50px) scale(1.1); }
  66% { transform: translate(-20px, 20px) scale(0.9); }
  100% { transform: translate(0px, 0px) scale(1); }
}

.animate-blob { animation: blob 7s infinite; }
.animation-delay-2000 { animation-delay: 2s; }
```

### Loader Animation
Custom loading spinner animation:

```css
.common-loader {
  height: 15px;
  aspect-ratio: 6;
  display: flex;
}

.common-loader:before,
.common-loader:after {
  content: "";
  flex: 1;
  padding-left: calc(100% / 6);
  background: radial-gradient(
    closest-side at calc(100% / 3) 50%,
    #000 90%,
    #0000
  ) 0/75% 100% content-box;
  animation: l20 2s infinite;
}

@keyframes l20 {
  0% { transform: scale(var(--_s, 1)) translate(0) rotate(0); }
  25% { transform: scale(var(--_s, 1)) translate(-25%) rotate(0); }
  50% { transform: scale(var(--_s, 1)) translate(-25%) rotate(1turn); }
  75%, 100% { transform: scale(var(--_s, 1)) translate(0) rotate(1turn); }
}
```

### Carousel Animation (Embla)
Horizontal scrolling carousel:

```css
.embla { overflow: hidden; }
.embla__container { 
  display: flex; 
  gap: 400px; 
}
.embla__slide { width: fit-content; }
```

## Component Styles

### Button Variants
```css
.primary-button {
  @apply bg-[#CAC5FE] z-50 text-black font-semibold rounded-full 
         hover:opacity-80 px-6 py-2 hover:bg-[#CAC5FE] text-[14px];
}

.btn-select {
  @apply bg-blue-200 text-black px-4 py-2 rounded;
}

.btn-deselect {
  @apply bg-white text-black px-4 py-2 rounded border;
}

.nav-btn {
  @apply rounded-full border border-transparent hover:border-black 
         hover:font-semibold text-[16px] leading-6 px-1 md:px-2.5 py-2.5;
}
```

### Header Styles
```css
.blue-head {
  @apply bg-blue-200 px-2 py-3 rounded-xl;
}
```

## Layout & Backgrounds

### Gradient Background
```css
.gradient {
  background: linear-gradient(135deg, #e8e9ea, #e7e9fb);
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}
```

## Responsive Design

The theme uses Tailwind's responsive prefixes:
- `sm:` for small screens (640px+)
- `md:` for medium screens (768px+)  
- `lg:` for large screens (1024px+)
- `xl:` for extra large screens (1280px+)
- `2xl:` for 2x extra large screens (1536px+)

## Accessibility Features

- Uses OKLCH color space for better contrast ratios
- Proper focus states with `outline-ring/50`
- Semantic color naming for consistent meaning
- Dark mode support with automatic contrast adjustment

## Implementation Notes

1. **CSS Variables**: All theme values are defined as CSS variables for easy customization
2. **Tailwind Integration**: Theme extends Tailwind's default theme configuration
3. **Dark Mode**: Automatic dark mode switching via `.dark` class
4. **Component Library**: Built with shadcn/ui components using New York style
5. **Animation Performance**: Uses hardware-accelerated transforms and opacity changes

## Usage Guidelines

- Use semantic color names (`primary`, `secondary`, `muted`, etc.) rather than direct hex values
- Apply animations sparingly for better performance
- Maintain consistent spacing using the defined radius scale
- Test all components in both light and dark modes
- Ensure proper contrast ratios meet WCAG accessibility standards

---

*Last Updated: Generated from current codebase*
*Framework: Next.js 14+ with App Router*
*Styling: Tailwind CSS with CSS Variables*
*Component Library: shadcn/ui*