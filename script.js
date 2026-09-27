'use strict';
document.documentElement.classList.add('js-enabled');

// Scientific equations transcribed from the active main.tex, not earlier drafts.
const equations = {
  point: String.raw`\min_{\|u\|_2=1}\mathbb E_\phi[\|H-u\|_2^2\mid Z=z]=2-2\|\mu_\phi(z)\|_2`,
  mean: String.raw`\mu_\phi(z)=\mathbb E_\phi[H\mid Z=z]`,
  noise: String.raw`\begin{gathered}x_t=a_tx+b_t\epsilon,\qquad v_t=a_t\epsilon-b_tx\\\epsilon\sim\mathcal N(0,I_d),\qquad a_t^2+b_t^2=1\end{gathered}`,
  prediction: String.raw`\widehat\epsilon_\theta=b_tx_t+a_tf_\theta(x_t,t,z)`,
  reward: String.raw`R_\theta(h,z)=-\frac12\int_{-8}^{8}\mathbb E_\epsilon\left\|\epsilon-\widehat\epsilon_\theta(x_\lambda,\lambda,z)\right\|_2^2\,\mathrm d\lambda`,
  snr: String.raw`\lambda=\log(a_t^2/b_t^2)`,
  bound: String.raw`\log p_\theta(h\mid z)\ge R_\theta(h,z)-c(h)`
};
if (window.katex) {
  document.querySelectorAll('[data-equation]').forEach((element) => {
    window.katex.render(equations[element.dataset.equation], element, {
      displayMode: element.classList.contains('equation'), throwOnError: false,
      output: 'htmlAndMathml', strict: 'error', trust: false
    });
  });
}

const menu = document.querySelector('.menu-toggle');
const navigation = document.getElementById('navigation');
menu.hidden = false;
function closeMenu() {
  menu.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('is-open');
}
menu.addEventListener('click', () => {
  const expanded = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(expanded));
  navigation.classList.toggle('is-open', expanded);
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
    closeMenu(); menu.focus();
  }
});

const navLinks = [...navigation.querySelectorAll('a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.find((entry) => entry.isIntersecting);
    if (!visible) return;
    navLinks.forEach((link) => {
      if (link.hash === `#${visible.target.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }, { rootMargin: '-15% 0px -65% 0px' });
  navLinks.forEach((link) => observer.observe(document.querySelector(link.hash)));
}

const copyButton = document.getElementById('copy-citation');
const copyStatus = document.getElementById('copy-status');
copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  const citation = document.getElementById('bibtex');
  try {
    if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(citation.textContent);
    copyStatus.textContent = citation.dataset.citationStatus === 'manuscript'
      ? 'Manuscript BibTeX copied.' : 'BibTeX copied.';
  } catch {
    const range = document.createRange();
    range.selectNodeContents(citation);
    const selection = window.getSelection();
    selection.removeAllRanges(); selection.addRange(range);
    copyStatus.textContent = 'BibTeX selected. Press ⌘C or Ctrl+C to copy.';
  }
});
