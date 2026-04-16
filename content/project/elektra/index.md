---
title: Elektra Autonomous Vehicle
type: page
show_toc: false
image:
  filename: elektra-car.png
summary: An experimental autonomous vehicle platform built at UAB with full perception, planning, and control systems.
tags: [Autonomous Driving, Computer Vision]
date: '2014-01-01'
links:
  - type: site
    url: 'https://adas.cvc.uab.es/elektra/'
    label: Project Website
---

<style>
.section-row {
  display: flex;
  flex-wrap: wrap;
  gap: 2.5rem;
  margin: 2.5rem 0;
  align-items: flex-start;
}
.section-row.reverse { flex-direction: row-reverse; }
.section-text { flex: 1; min-width: 300px; }
.section-media { flex: 0 0 calc(45% - 1.25rem); }

@media (max-width: 1024px) {
  .section-row, .section-row.reverse { flex-direction: column; }
  .section-media { flex: 1 1 100%; }
}

.section-slideshow {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  background: #f5f5f5;
}
.section-slideshow-container {
  position: relative;
  width: 100%;
  padding-bottom: 75%;
  height: 0;
}
.section-slideshow-image {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.6s ease-in-out;
}
.section-slideshow-image.active { opacity: 1; }
.section-slideshow-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.slideshow-nav {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.5rem;
  z-index: 10;
}
.slideshow-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
  cursor: pointer;
  border: none;
  transition: background 0.3s;
}
.slideshow-dot.active { background: white; }
.slideshow-caption {
  position: absolute;
  bottom: 2.5rem;
  left: 0; right: 0;
  padding: 0.5rem 1rem;
  background: rgba(0,0,0,0.45);
  color: white;
  font-size: 0.85rem;
  text-align: center;
  z-index: 5;
}

.elektra-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin: 2rem 0;
  text-align: center;
}
.elektra-stat {
  padding: 1.25rem;
  background: #f5f5f5;
  border-radius: 8px;
}
.dark .elektra-stat { background: #2a2a2a; }
.elektra-stat-value { font-size: 1.6rem; font-weight: 700; color: #333; }
.dark .elektra-stat-value { color: #eee; }
.elektra-stat-label { font-size: 0.85rem; color: #666; margin-top: 0.4rem; }
.dark .elektra-stat-label { color: #bbb; }
@media (max-width: 640px) { .elektra-stats { grid-template-columns: repeat(2, 1fr); } }

.featured-video-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.75rem;
  background: rgb(var(--color-primary-600));
  color: white;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  margin: 1.25rem 0;
  transition: background 0.2s;
}
.featured-video-btn:hover { background: rgb(var(--color-primary-700)); }

.video-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.5rem;
}
.video-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.9rem;
  border: 1px solid rgba(0,0,0,0.15);
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  background: none;
  color: inherit;
  font-family: inherit;
  transition: border-color 0.2s, background 0.2s;
}
.video-link-btn:hover { border-color: rgb(var(--color-primary-500)); background: rgba(var(--color-primary-50), 0.5); }
.dark .video-link-btn { border-color: rgba(255,255,255,0.15); }
.dark .video-link-btn:hover { border-color: rgb(var(--color-primary-400)); background: rgba(255,255,255,0.05); }

.video-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.8);
  z-index: 1000;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.video-modal.active { display: flex; }
.video-modal-content {
  background: white;
  border-radius: 12px;
  max-width: 900px;
  width: 100%;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}
.dark .video-modal-content { background: #1a1a1a; }
.video-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #e5e5e5;
}
.dark .video-modal-header { border-bottom-color: #333; }
.video-modal-title { font-size: 1rem; font-weight: 600; margin: 0; }
.video-modal-close {
  background: none;
  border: none;
  font-size: 1.4rem;
  cursor: pointer;
  color: #666;
  line-height: 1;
  padding: 0.25rem 0.5rem;
}
.dark .video-modal-close { color: #aaa; }
.video-modal-player {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
}
.video-modal-player iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}
</style>

<div id="video-modal" class="video-modal">
  <div class="video-modal-content">
    <div class="video-modal-header">
      <h3 class="video-modal-title" id="video-modal-title">Video</h3>
      <button class="video-modal-close" onclick="closeVideoModal()">✕</button>
    </div>
    <div class="video-modal-player">
      <iframe id="video-modal-player" src="" frameborder="0" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
    </div>
  </div>
</div>

<script>
let slideIndex = {};
let autoPlayTimer = {};

const slideCaptions = {
  project:    ["Elektra autonomous vehicle platform", "Multidisciplinary team composition"],
  perception: ["Real-time stereo vision processing", "3D scene reconstruction", "Free-space detection", "Pedestrian detection"],
  synthia:    ["SYNTHIA daytime urban scenario", "SYNTHIA nighttime driving"]
};

function initSlideshow(id, n) {
  slideIndex[id] = 1;
  showSlides(1, id);
  autoPlay(id);
}
function currentSlide(n, id) {
  clearTimeout(autoPlayTimer[id]);
  showSlides(slideIndex[id] = n, id);
  autoPlay(id);
}
function showSlides(n, id) {
  const el = document.getElementById(id + '-slideshow');
  if (!el) return;
  const slides = el.querySelectorAll('.section-slideshow-image');
  const dots   = el.querySelectorAll('.slideshow-dot');
  const cap    = document.getElementById(id + '-caption');
  if (n > slides.length) slideIndex[id] = 1;
  if (n < 1) slideIndex[id] = slides.length;
  slides.forEach(s => s.classList.remove('active'));
  dots.forEach(d => d.classList.remove('active'));
  if (slides.length) {
    slides[slideIndex[id] - 1].classList.add('active');
    if (dots.length) dots[slideIndex[id] - 1].classList.add('active');
    if (cap && slideCaptions[id]) cap.textContent = slideCaptions[id][slideIndex[id] - 1];
  }
}
function autoPlay(id) {
  autoPlayTimer[id] = setTimeout(() => {
    slideIndex[id]++;
    showSlides(slideIndex[id], id);
    autoPlay(id);
  }, 5000);
}
function openVideoModal(videoId, title) {
  document.getElementById('video-modal-title').textContent = title;
  document.getElementById('video-modal-player').src = `https://www.youtube.com/embed/${videoId}`;
  document.getElementById('video-modal').classList.add('active');
  document.body.style.overflow = 'hidden';
}
function closeVideoModal() {
  document.getElementById('video-modal').classList.remove('active');
  document.getElementById('video-modal-player').src = '';
  document.body.style.overflow = '';
}
document.addEventListener('click', e => {
  if (e.target === document.getElementById('video-modal')) closeVideoModal();
});
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeVideoModal(); });
</script>

<div class="elektra-stats">
  <div class="elektra-stat"><div class="elektra-stat-value">20+</div><div class="elektra-stat-label">Top-tier Publications</div></div>
  <div class="elektra-stat"><div class="elektra-stat-value">8</div><div class="elektra-stat-label">Partner Institutions</div></div>
  <div class="elektra-stat"><div class="elektra-stat-value">400 FPS</div><div class="elektra-stat-label">Real-time Stixel</div></div>
  <div class="elektra-stat"><div class="elektra-stat-value">2010s</div><div class="elektra-stat-label">Active Period</div></div>
</div>

---

## Autonomous Driving in Action

Watch the Elektra platform navigate urban roads autonomously — perception, planning, and control integrated end-to-end:

<button class="featured-video-btn" onclick="openVideoModal('tvZnN65jbCE', 'On-Road Autonomous Driving Demo')">▶ Watch Autonomous Driving Demo</button>

---

## Project Overview

**Elektra** is an autonomous driving platform and the **Catalan hub of autonomous driving**, bringing together more than **20 professionals** from academia and industry. The platform integrates perception, planning, control, and communications to demonstrate production-ready autonomous driving in urban environments.

<div class="section-row">
  <div class="section-text">

**Partner institutions:**
- **CVC-UAB** — Environment perception & computer vision
- **CAOS-UAB** — Embedded hardware & GPU optimization
- **UPC-Tarrasa** — Control & path planning
- **CTTC-UPC** — Positioning & localization
- **UAB-DEIC** — Vehicle-to-vehicle communications
- **UAB-CEPHIS** — Electronics & integration
- **CT Ingenieros** — Vehicle engineering & drive-by-wire
- **Municipality of Sant Quirze** — Test track facility

The **Computer Vision Center (CVC)** led the perception stack — my primary contribution to the project. Validation was performed at the Sant Quirze test track and in urban environments, demonstrating the system across controlled and real-world scenarios.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="project-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="elektra-car.png" alt="Elektra autonomous vehicle platform">
        </div>
        <div class="section-slideshow-image">
          <img src="overview.png" alt="Project team and institution overview">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'project')"></button>
          <button class="slideshow-dot" onclick="currentSlide(2, 'project')"></button>
        </div>
        <div class="slideshow-caption" id="project-caption">Elektra autonomous vehicle platform</div>
      </div>
    </div>
  </div>
</div>

<script>initSlideshow('project', 2);</script>

---

## Perception System

I **initiated and led the full perception pipeline** — from raw sensor data to high-level scene understanding. The system fuses multiple modalities for robust environmental awareness:

<div class="section-row reverse">
  <div class="section-text">

**Obstacle & Pedestrian Detection**
Real-time CNN-based detection running at 400+ FPS on GPU hardware, with multi-scale detection for obstacles at various distances and temporal consistency across frames.

**Free Space & Lane Detection**
Stixel-based 3D scene representation identifies drivable areas and lane boundaries from dense stereo depth. Adaptive thresholding handles varying road conditions in real time.

**3D Reconstruction & SLAM**
Stereo cameras provide dense depth estimation. Visual odometry and loop closure detection enable robust 6-DOF localization even in GPS-denied environments (tunnels, urban canyons).

**Sensor Fusion**
Stereo cameras, monocular vision, LIDAR, and IMU are combined for redundant, accurate scene understanding optimized for embedded automotive hardware.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="perception-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="image1.png" alt="Real-time stereo vision processing">
        </div>
        <div class="section-slideshow-image">
          <img src="image102.png" alt="3D scene reconstruction">
        </div>
        <div class="section-slideshow-image">
          <img src="image97.png" alt="Free-space detection">
        </div>
        <div class="section-slideshow-image">
          <img src="image104.png" alt="Pedestrian detection">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'perception')"></button>
          <button class="slideshow-dot" onclick="currentSlide(2, 'perception')"></button>
          <button class="slideshow-dot" onclick="currentSlide(3, 'perception')"></button>
          <button class="slideshow-dot" onclick="currentSlide(4, 'perception')"></button>
        </div>
        <div class="slideshow-caption" id="perception-caption">Real-time stereo vision processing</div>
      </div>
    </div>
  </div>
</div>

<script>initSlideshow('perception', 4);</script>

---

## SYNTHIA: Synthetic Data for Autonomous Driving

**SYNTHIA** is a synthetic data generation framework I developed within the Elektra project that creates photorealistic, automatically labeled driving scenarios — addressing the fundamental bottleneck of acquiring large-scale annotated driving data.

<div class="section-row">
  <div class="section-text">

**Capabilities:**
- Multiple environmental conditions: day, night, rain, fog, snow
- Diverse urban scenes: intersections, pedestrian crossings, parked vehicles
- Automatic ground-truth labels for semantic segmentation, depth, and optical flow
- Scalable: thousands of labeled frames in hours

**Impact:**
SYNTHIA powered the Elektra perception pipeline, reducing the need for expensive field data collection and enabling systematic testing across conditions that are rare or dangerous to capture in the real world. Results were published at CVPR, ICCV, and ECCV. The dataset was licensed to Intel, Audi, and Huawei.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="synthia-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="synthia-360.png" alt="SYNTHIA daytime urban scenario">
        </div>
        <div class="section-slideshow-image">
          <img src="synthia-overview.png" alt="SYNTHIA multi-condition overview">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'synthia')"></button>
          <button class="slideshow-dot" onclick="currentSlide(2, 'synthia')"></button>
        </div>
        <div class="slideshow-caption" id="synthia-caption">SYNTHIA daytime urban scenario</div>
      </div>
    </div>
  </div>
</div>

<script>initSlideshow('synthia', 2);</script>

---

## Publications & Impact

The Elektra project generated **20+ peer-reviewed publications** at top venues including CVPR, ICCV, ECCV, IEEE TITS, and IEEE T-IV. Key contributions include:

- **Stixel-based 3D scene understanding** — efficient real-time scene representation
- **SYNTHIA dataset** — synthetic data for autonomous driving, widely used in the community
- **Semantic segmentation** pipelines for urban scene understanding
- **Domain adaptation** methods bridging synthetic and real data

**Legacy:** Elektra proved vision-centric autonomous driving is achievable in real urban conditions and produced benchmark datasets still used by the research community. Alumni of the team now work at leading autonomous driving companies worldwide.

---

## Selected Videos

<div class="video-links">
  <button class="video-link-btn" onclick="openVideoModal('tvZnN65jbCE', 'Autonomous Driving Demo')">▶ Autonomous Driving Demo</button>
  <button class="video-link-btn" onclick="openVideoModal('FWM-5Ps8zFo', 'Elektra Project Overview')">▶ Project Overview</button>
  <button class="video-link-btn" onclick="openVideoModal('7u-mMtm1Q9o', 'Person Detection')">▶ Person Detection</button>
</div>
