// === 沪教版课件 - 公共交互脚本 ===

// Answer toggle
function showAnswer(id) {
  const el = document.getElementById('answer-' + id);
  if (!el) return;
  el.classList.toggle('show');
  // Check selected answer
  const selected = document.querySelector('input[name="q' + id + '"]:checked');
  const correctKey = el.getAttribute('data-correct');
  if (selected && correctKey) {
    if (selected.value === correctKey) {
      el.classList.add('correct');
      el.classList.remove('wrong');
    } else {
      el.classList.add('wrong');
      el.classList.remove('correct');
    }
  }
}

// Tab switching
function switchTab(evt, tabGroup, tabContent) {
  const buttons = document.querySelectorAll('[data-tab-group="' + tabGroup + '"]');
  buttons.forEach(b => b.classList.remove('active'));
  evt.target.classList.add('active');
  
  const contents = document.querySelectorAll('[data-tab-content="' + tabGroup + '"]');
  contents.forEach(c => c.style.display = 'none');
  document.getElementById(tabContent).style.display = 'block';
}

// Initialize tab content visibility
document.addEventListener('DOMContentLoaded', function() {
  // Hide all tab contents except first
  document.querySelectorAll('[data-tab-content]').forEach((el, i) => {
    if (i > 0) el.style.display = 'none';
  });
});

// Scroll-based section highlight
document.addEventListener('DOMContentLoaded', function() {
  const sections = document.querySelectorAll('[data-section]');
  const links = document.querySelectorAll('.sidebar a[data-section]');
  
  if (sections.length === 0 || links.length === 0) return;
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        links.forEach(l => l.classList.remove('active'));
        const active = document.querySelector('.sidebar a[data-section="' + entry.target.getAttribute('data-section') + '"]');
        if (active) active.classList.add('active');
      }
    });
  }, { threshold: 0.3 });
  
  sections.forEach(s => observer.observe(s));
});
