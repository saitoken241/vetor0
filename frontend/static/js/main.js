/* ============================================================
    VETOR0 · Interações
   ============================================================ */
"use strict";

/* ---------- Header: borda ao rolar ---------- */
const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 8);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

/* ---------- Menu mobile ---------- */
const navToggle = document.getElementById("nav-toggle");
const siteNav = document.getElementById("site-nav");

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const aberto = siteNav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(aberto));
    navToggle.setAttribute("aria-label", aberto ? "Fechar menu" : "Abrir menu");
  });

  siteNav.querySelectorAll("a").forEach((link) =>
    link.addEventListener("click", () => {
      siteNav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    })
  );
}

/* ---------- Reveal ao entrar na viewport ---------- */
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

/* ---------- Contadores animados ---------- */
function animateCounter(el) {
  const target = Number(el.dataset.target || 0);
  const suffix = el.dataset.suffix || "";
  const duration = 2200;
  const start = performance.now();

  function tick(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 4); // ease-out quart
    el.textContent = Math.round(target * eased).toLocaleString("pt-BR") + suffix;
    if (progress < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

const counterObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.5 }
);
document.querySelectorAll(".stat-number").forEach((el) => counterObserver.observe(el));

/* ---------- Terminal do hero: efeito de digitação ---------- */
const lines = Array.from(document.querySelectorAll(".terminal-line"));

async function typeLine(el, text, delay = 900) {
  el.textContent = "";
  for (const ch of text) {
    el.textContent += ch;
    // digitação com ritmo irregular, como quem escreve de verdade
    const pausa = ch === " " ? 60 : 40 + Math.random() * 40;
    await new Promise((r) => setTimeout(r, pausa));
  }
  el.dataset.done = "true";
  await new Promise((r) => setTimeout(r, delay));
}

async function runTerminal() {
  if (!lines.length) return;
  await new Promise((r) => setTimeout(r, 1200));
  for (const el of lines) {
    const text = el.dataset.text || "";
    await typeLine(el, text, el.classList.contains("terminal-final") ? 1400 : 900);
  }
}

if (lines.length) {
  if ("IntersectionObserver" in window) {
    const terminalObserver = new IntersectionObserver(
      (entries) => {
        if (entries.some((e) => e.isIntersecting)) {
          terminalObserver.disconnect();
          runTerminal();
        }
      },
      { threshold: 0.3 }
    );
    terminalObserver.observe(lines[0]);
  } else {
    runTerminal();
  }
}

/* ---------- Marquee: só inicia após as fontes carregarem ---------- */
/* Sem isso, a fonte chega depois, a largura da faixa muda e o loop "pula". */
const marqueeTrack = document.querySelector(".marquee-track");
if (marqueeTrack) {
  const iniciarMarquee = () => marqueeTrack.classList.add("is-running");
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(iniciarMarquee);
  } else {
    iniciarMarquee();
  }
}

/* ---------- Ano no rodapé ---------- */
const ano = document.getElementById("ano");
if (ano) ano.textContent = new Date().getFullYear();

/* ============================================================
   Formulário de contato
   ============================================================ */
const form = document.getElementById("form-contato");

if (form) {
  const statusBox = document.getElementById("form-status");
  const btnEnviar = document.getElementById("btn-enviar");

  function setError(fieldId, message) {
    const field = form.querySelector(`#${fieldId}`);
    const errorEl = form.querySelector(`[data-error-for="${fieldId}"]`);
    if (field) field.closest(".form-field")?.classList.toggle("has-error", Boolean(message));
    if (errorEl) {
      errorEl.textContent = message || "";
      errorEl.classList.toggle("is-visible", Boolean(message));
    }
  }

  function validate() {
    let ok = true;
    const nome = form.nome.value.trim();
    const email = form.email.value.trim();
    const assunto = form.assunto.value;
    const mensagem = form.mensagem.value.trim();
    const consentimento = form.consentimento.checked;

    setError("nome", nome.length < 2 ? "Informe seu nome (mín. 2 caracteres)." : "");
    setError("email", /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) ? "" : "Informe um e-mail válido.");
    setError("assunto", assunto ? "" : "Selecione o serviço de interesse.");
    setError("mensagem", mensagem.length < 10 ? "Descreva sua necessidade (mín. 10 caracteres)." : "");
    setError("consentimento", consentimento ? "" : "É necessário aceitar o uso dos dados (LGPD).");

    ok = nome.length >= 2 && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) && assunto !== "" && mensagem.length >= 10 && consentimento;
    return ok;
  }

  form.querySelectorAll("input, select, textarea").forEach((el) =>
    el.addEventListener("input", () => {
      const id = el.id;
      if (id) setError(id, "");
    })
  );

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    statusBox.className = "form-status";
    statusBox.textContent = "";

    if (!validate()) {
      statusBox.classList.add("is-error");
      statusBox.textContent = "Revise os campos destacados e tente novamente.";
      return;
    }

    const payload = {
      nome: form.nome.value.trim(),
      email: form.email.value.trim(),
      empresa: form.empresa.value.trim(),
      telefone: form.telefone.value.trim(),
      assunto: form.assunto.value,
      mensagem: form.mensagem.value.trim(),
      consentimento: form.consentimento.checked,
    };

    btnEnviar.disabled = true;
    btnEnviar.textContent = "Enviando…";

    try {
      const resposta = await fetch("/api/contato", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const corpo = await resposta.json();

      if (resposta.ok && corpo.ok) {
        statusBox.classList.add("is-success");
        statusBox.textContent = `✓ ${corpo.message} Protocolo: ${corpo.protocolo}.`;
        form.reset();
      } else {
        statusBox.classList.add("is-error");
        statusBox.textContent =
          corpo.detail?.[0]?.msg || corpo.detail || "Não foi possível enviar. Tente novamente.";
      }
    } catch (erro) {
      statusBox.classList.add("is-error");
      statusBox.textContent = "Falha de conexão. Verifique sua internet e tente novamente.";
    } finally {
      btnEnviar.disabled = false;
      btnEnviar.textContent = "Enviar mensagem";
    }
  });
}
