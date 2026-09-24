/* jsm85.github.io — mobile nav, art filters, lightbox.
   No dependencies. Everything degrades to working HTML without it. */
(function () {
  "use strict";

  /* ── Mobile nav ─────────────────────────────────────── */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });

    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ── Art filters ────────────────────────────────────── */
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip[data-filter]"));
  var tiles = Array.prototype.slice.call(document.querySelectorAll(".art-tile"));

  if (chips.length && tiles.length) {
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var filter = chip.getAttribute("data-filter");

        chips.forEach(function (c) { c.classList.toggle("is-active", c === chip); });
        tiles.forEach(function (tile) {
          tile.hidden = filter !== "all" && tile.getAttribute("data-medium") !== filter;
        });
      });
    });
  }

  /* ── Lightbox ───────────────────────────────────────── */
  var box = document.getElementById("lightbox");

  if (box && tiles.length) {
    var img = box.querySelector(".lightbox__img");
    var elTitle = box.querySelector(".lightbox__title");
    var elMeta = box.querySelector(".lightbox__meta");
    var elCap = box.querySelector(".lightbox__caption");
    var btnClose = box.querySelector(".lightbox__close");
    var btnPrev = box.querySelector(".lightbox__nav--prev");
    var btnNext = box.querySelector(".lightbox__nav--next");

    var buttons = Array.prototype.slice.call(document.querySelectorAll(".art-tile__btn"));
    var current = 0;
    var opener = null;

    var visibleIndexes = function () {
      return buttons.reduce(function (acc, btn, i) {
        if (!btn.closest(".art-tile").hidden) acc.push(i);
        return acc;
      }, []);
    };

    var show = function (index) {
      var btn = buttons[index];
      if (!btn) return;

      current = index;

      // Nothing to step through when only one piece is on show.
      var single = visibleIndexes().length < 2;
      btnPrev.hidden = single;
      btnNext.hidden = single;

      img.src = btn.getAttribute("data-full");
      img.alt = btn.querySelector("img") ? btn.querySelector("img").alt : "";
      elTitle.textContent = btn.getAttribute("data-title") || "";
      elMeta.textContent = btn.getAttribute("data-meta") || "";
      elCap.textContent = btn.getAttribute("data-caption") || "";
    };

    var step = function (dir) {
      var pool = visibleIndexes();
      if (pool.length < 2) return;

      var at = pool.indexOf(current);
      show(pool[(at + dir + pool.length) % pool.length]);
    };

    var close = function () {
      box.hidden = true;
      document.body.style.overflow = "";
      if (opener) opener.focus();
    };

    var open = function (index, from) {
      opener = from;
      show(index);
      box.hidden = false;
      document.body.style.overflow = "hidden";
      btnClose.focus();
    };

    buttons.forEach(function (btn, i) {
      btn.addEventListener("click", function () { open(i, btn); });
    });

    btnClose.addEventListener("click", close);
    btnPrev.addEventListener("click", function () { step(-1); });
    btnNext.addEventListener("click", function () { step(1); });

    box.addEventListener("click", function (e) {
      if (e.target === box || e.target.classList.contains("lightbox__figure")) close();
    });

    document.addEventListener("keydown", function (e) {
      if (box.hidden) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
    });
  }
})();
