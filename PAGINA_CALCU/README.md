# Proyecto Calculadora - Demo Interna (Talento Lab) ⚙️

Este proyecto contiene la estructura estática de la nueva calculadora web, preparada específicamente para la automatización con **Selenium**.

## 📂 Estructura del Entregable
- `index.html`: Estructura semántica con IDs y Names únicos.
- `estilos.css`: Diseño visual minimalista.
- `selectors.md`: Documentación técnica de los selectores CSS para los scripts de automatización.

## 🚀 Guía de Verificación Rápida (Para Silvia)

Para comprobar que los elementos son unívocos y están listos para Selenium, seguir estos pasos:

1. **Abrir el archivo**: Abrir `index.html` en cualquier navegador (Chrome recomendado).
2. **Abrir DevTools**: Presionar `F12` o `Clic derecho > Inspeccionar`.
3. **Validar Selectores**: Copiar y pegar los siguientes comandos en la **Console** para verificar la puntería de los selectores:

   * **Campo Número 1**:
     ```javascript
     document.querySelector('#num1').style.border = '3px solid red';
     ```
   * **Campo Email**:
     ```javascript
     document.querySelector('input[name="email"]').style.background = 'yellow';
     ```
   * **Botón Enviar**:
     ```javascript
     document.querySelector('.btn.enviar').innerText = 'IDENTIFICADO';
     ```

## 🛠️ Notas Técnicas
- **IDs únicos**: Se han asignado IDs siguiendo la convención *kebab-case* (ej. `acepta-condiciones`).
- **Sin JavaScript**: La página es 100% estática según lo solicitado, permitiendo que la lógica sea inyectada o probada externamente.
- **Selectores Estables**: Se priorizaron IDs y Atributos Name para evitar la fragilidad de los tests ante cambios en el diseño CSS.

---
*Desarrollado por Yamila - Equipo de Automation QA*