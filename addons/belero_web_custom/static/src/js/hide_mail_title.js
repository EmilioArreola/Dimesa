/** @odoo-module **/

console.log("▶️ [belero_web_custom] hide_mail_title.js cargado");

const NEW_TITLE_TEXT = "Enviar correo al cliente";
const APPLIED_FLAG = "data-custom-title-applied";

function applyToModalHeader(header) {
    if (!header) return;
    const title = header.querySelector("h4.modal-title");
    if (!title) return;

    // Si ya aplicamos, aseguramos que el nuevo título exista y el original esté oculto
    if (header.closest(".modal")?.hasAttribute(APPLIED_FLAG)) {
        if (title.style.display !== "none") title.style.display = "none";
        if (!header.querySelector(".custom-mail-title")) {
            const nt = document.createElement("div");
            nt.className = "custom-mail-title";
            nt.textContent = NEW_TITLE_TEXT;
            styleNewTitle(nt);
            header.appendChild(nt);
        }
        return;
    }

    // Solo actuamos si el texto original es exactamente "Odoo"
    if (title.textContent && title.textContent.trim() === "Odoo") {
        title.style.display = "none"; // Ocultar original

        if (!header.querySelector(".custom-mail-title")) {
            const newTitle = document.createElement("div");
            newTitle.className = "custom-mail-title";
            newTitle.textContent = NEW_TITLE_TEXT;
            styleNewTitle(newTitle);
            header.appendChild(newTitle);
        }

        const modal = header.closest(".modal");
        if (modal) modal.setAttribute(APPLIED_FLAG, "1");
        console.log("✅ [belero_web_custom] título reemplazado en modal");
    }
}

function styleNewTitle(node) {
    node.style.fontSize = "18px";
    node.style.fontWeight = "600";
    node.style.color = "#333";
    node.style.textAlign = "center";
    node.style.width = "100%";
    node.style.marginTop = "4px";
}

// Observador sobre cambios en el DOM: detecta creación de modales y re-renderizados
const observer = new MutationObserver(() => {
    document.querySelectorAll("header.modal-header").forEach((header) => {
        try {
            applyToModalHeader(header);
        } catch (e) {
            console.error("[belero_web_custom] error applying title:", e);
        }
    });
});

// Iniciar observer
observer.observe(document.body, { childList: true, subtree: true });

// También ejecutamos una pasada inmediata por si el modal ya está en DOM
setTimeout(() => {
    document.querySelectorAll("header.modal-header").forEach((header) => {
        applyToModalHeader(header);
    });
}, 300);
