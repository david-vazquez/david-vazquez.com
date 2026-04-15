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
/* Alternating layout: text on left/right with images, proper text wrapping */
.section-row {
  display: flex;
  flex-wrap: wrap;
  gap: 2.5rem;
  margin: 3rem 0;
  align-items: flex-start;
}

.section-row.reverse {
  flex-direction: row-reverse;
}

.section-text {
  flex: 1;
  min-width: 300px;
}

.section-media {
  flex: 0 0 calc(45% - 1.25rem);
}

/* When text is longer, make it span full width below */
@media (max-width: 1024px) {
  .section-row {
    flex-direction: column;
  }
  .section-row.reverse {
    flex-direction: column;
  }
  .section-media {
    flex: 1 1 100%;
  }
}

/* Slideshow container */
.section-slideshow {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  background: #f5f5f5;
  margin: 0;
}

.section-slideshow-container {
  position: relative;
  width: 100%;
  padding-bottom: 75%;
  height: 0;
}

.section-slideshow-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.6s ease-in-out;
}

.section-slideshow-image.active {
  opacity: 1;
}

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
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.6);
  cursor: pointer;
  border: none;
  transition: background 0.3s;
}

.slideshow-dot.active {
  background: rgba(255, 255, 255, 1);
}

.slideshow-dot:hover {
  background: rgba(255, 255, 255, 0.9);
}

.slideshow-caption {
  position: absolute;
  bottom: 3.5rem;
  left: 0;
  right: 0;
  padding: 0.75rem 1rem;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  font-size: 0.9rem;
  text-align: center;
  z-index: 5;
}

/* Section video carousel - full width below text+image */
.section-video-carousel {
  margin: 2.5rem 0 0;
  padding: 2rem;
  border-top: 1px solid #e5e5e5;
  width: 100%;
  clear: both;
  background: #fafafa;
  border-radius: 8px;
}

.dark .section-video-carousel {
  border-top-color: #333;
  background: #1a1a1a;
}

.section-video-carousel h4 {
  font-size: 0.9rem;
  margin: 0 0 1rem 0;
  color: #333;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
}

.dark .section-video-carousel h4 {
  color: #e5e5e5;
}

.section-carousel-thumbnails {
  display: flex;
  gap: 0.75rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
  scroll-behavior: smooth;
}

.section-carousel-thumbnails::-webkit-scrollbar {
  height: 6px;
}

.section-carousel-thumbnails::-webkit-scrollbar-track {
  background: transparent;
  border-radius: 3px;
}

.section-carousel-thumbnails::-webkit-scrollbar-thumb {
  background: #ccc;
  border-radius: 3px;
}

.section-carousel-thumbnails::-webkit-scrollbar-thumb:hover {
  background: #999;
}

.dark .section-carousel-thumbnails::-webkit-scrollbar-track {
  background: transparent;
}

.dark .section-carousel-thumbnails::-webkit-scrollbar-thumb {
  background: #555;
}

.dark .section-carousel-thumbnails::-webkit-scrollbar-thumb:hover {
  background: #777;
}

.section-video-thumb {
  flex: 0 0 120px;
  cursor: pointer;
  border-radius: 4px;
  overflow: hidden;
  border: 2px solid #ddd;
  transition: all 0.2s;
  position: relative;
  background: #f9f9f9;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-video-thumb:hover {
  border-color: var(--primary-600, #3b82f6);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.dark .section-video-thumb {
  border-color: #444;
  background: #2a2a2a;
}

.dark .section-video-thumb:hover {
  border-color: var(--primary-500, #6366f1);
}

.section-video-thumb::before {
  content: '▶';
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: rgba(59, 130, 246, 0.6);
  z-index: 1;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s;
  background: rgba(255, 255, 255, 0.8);
}

.section-video-thumb:hover::before {
  opacity: 1;
}

.dark .section-video-thumb::before {
  color: rgba(99, 102, 241, 0.8);
  background: rgba(0, 0, 0, 0.3);
}


.section-video-thumb img {
  width: 100%;
  height: 68px;
  object-fit: cover;
  display: block;
  background: linear-gradient(135deg, #e5e5e5 0%, #f0f0f0 100%);
}

.dark .section-video-thumb img {
  background: linear-gradient(135deg, #2a2a2a 0%, #333 100%);
}

.section-video-thumb p {
  padding: 0.4rem;
  background: #f9f9f9;
  font-size: 0.65rem;
  line-height: 1.2;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  margin: 0;
  color: #333;
  font-weight: 500;
}

.dark .section-video-thumb p {
  background: #333;
  color: #e5e5e5;
}

/* Video modal popup */
.video-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  z-index: 1000;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.video-modal.active {
  display: flex;
}

.video-modal-content {
  background: white;
  border-radius: 12px;
  max-width: 900px;
  width: 100%;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

.dark .video-modal-content {
  background: #1a1a1a;
}

.video-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #e5e5e5;
}

.dark .video-modal-header {
  border-bottom-color: #333;
}

.video-modal-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0;
}

.video-modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
  padding: 0.5rem;
}

.dark .video-modal-close {
  color: #aaa;
}

.video-modal-close:hover {
  color: #333;
}

.dark .video-modal-close:hover {
  color: #fff;
}

.video-modal-player {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  width: 100%;
}

.video-modal-player iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Key Metrics */
.elektra-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin: 2.5rem 0;
  text-align: center;
}

.elektra-stat {
  padding: 1.5rem;
  background: #f5f5f5;
  border-radius: 8px;
}

.elektra-stat-value {
  font-size: 1.8rem;
  font-weight: 700;
  color: #333;
}

.elektra-stat-label {
  font-size: 0.9rem;
  color: #666;
  margin-top: 0.5rem;
}

.dark .elektra-stat {
  background: #2a2a2a;
}

.dark .elektra-stat-value {
  color: #eee;
}

.dark .elektra-stat-label {
  color: #bbb;
}

/* Featured demo button */
.featured-video-btn {
  display: inline-block;
  padding: 1rem 2rem;
  background: var(--primary-600, #3b82f6);
  color: white;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: background 0.2s;
  border: none;
  margin: 1.5rem 0;
}

.featured-video-btn:hover {
  background: var(--primary-700, #2563eb);
}

.dark .featured-video-btn {
  background: var(--primary-500, #6366f1);
}

.dark .featured-video-btn:hover {
  background: var(--primary-600, #4f46e5);
}

@media (max-width: 768px) {
  .section-row {
    grid-template-columns: 1fr;
  }
  .elektra-stats {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

<!-- Video Modal Popup -->
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
  project: ["Elektra autonomous vehicle platform", "Multidisciplinary team composition"],
  perception: ["Real-time stereo vision processing", "3D scene reconstruction"],
  synthia: ["SYNTHIA daytime urban scenario", "SYNTHIA nighttime driving"],
  vehicle: ["Custom vehicle electronics", "GPU-accelerated processing"],
  control: ["Low-level motion control", "Vehicle actuator integration"]
};

function initSlideshow(slideshowId, numSlides) {
  slideIndex[slideshowId] = 1;
  autoPlayTimer[slideshowId] = null;
  showSlides(1, slideshowId);
  autoPlay(slideshowId);
}

function currentSlide(n, slideshowId) {
  clearTimeout(autoPlayTimer[slideshowId]);
  showSlides(slideIndex[slideshowId] = n, slideshowId);
  autoPlay(slideshowId);
}

function showSlides(n, slideshowId) {
  const slideshow = document.getElementById(slideshowId + '-slideshow');
  if (!slideshow) return;
  
  const slides = slideshow.querySelectorAll('.section-slideshow-image');
  const dots = slideshow.querySelectorAll('.slideshow-dot');
  const caption = document.getElementById(slideshowId + '-caption');
  
  if (n > slides.length) { slideIndex[slideshowId] = 1; }
  if (n < 1) { slideIndex[slideshowId] = slides.length; }
  
  slides.forEach(slide => slide.classList.remove('active'));
  dots.forEach(dot => dot.classList.remove('active'));
  
  if (slides.length > 0) {
    slides[slideIndex[slideshowId] - 1].classList.add('active');
    if (dots.length > 0) dots[slideIndex[slideshowId] - 1].classList.add('active');
    if (caption && slideCaptions[slideshowId]) {
      caption.textContent = slideCaptions[slideshowId][slideIndex[slideshowId] - 1];
    }
  }
}

function autoPlay(slideshowId) {
  autoPlayTimer[slideshowId] = setTimeout(() => {
    slideIndex[slideshowId]++;
    showSlides(slideIndex[slideshowId], slideshowId);
    autoPlay(slideshowId);
  }, 5000);
}

function openVideoModal(videoId, videoTitle) {
  const modal = document.getElementById('video-modal');
  const player = document.getElementById('video-modal-player');
  const titleEl = document.getElementById('video-modal-title');
  
  titleEl.textContent = videoTitle;
  player.src = `https://www.youtube.com/embed/${videoId}`;
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
  const modal = document.getElementById('video-modal');
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

document.addEventListener('click', function(event) {
  const modal = document.getElementById('video-modal');
  const content = document.querySelector('.video-modal-content');
  if (event.target === modal) {
    closeVideoModal();
  }
});

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeVideoModal();
  }
});
</script>

<!-- Key Metrics -->
<div class="elektra-stats">
  <div class="elektra-stat">
    <div class="elektra-stat-value">20+</div>
    <div class="elektra-stat-label">Top-tier Publications</div>
  </div>
  <div class="elektra-stat">
    <div class="elektra-stat-value">3</div>
    <div class="elektra-stat-label">Universities</div>
  </div>
  <div class="elektra-stat">
    <div class="elektra-stat-value">400 FPS</div>
    <div class="elektra-stat-label">Real-time Stixel</div>
  </div>
  <div class="elektra-stat">
    <div class="elektra-stat-value">2010s</div>
    <div class="elektra-stat-label">Active Period</div>
  </div>
</div>

---

## Autonomous Driving in Action

The Elektra platform demonstrates **real-world autonomous capabilities** — from perception-to-control integration across urban driving scenarios. Watch the full autonomous driving demonstration:

<button class="featured-video-btn" onclick="openVideoModal('tvZnN65jbCE', 'On-Road Autonomous Driving Demo')">▶ Watch Full Autonomous Driving Demo</button>

---

## Project Overview

**Elektra** is an autonomous driving platform positioned as the **Catalan hub of autonomous driving**, bringing together more than **20 professionals** from diverse backgrounds across academia and industry.

<div class="section-row">
  <div class="section-text">

**A Multidisciplinary Ecosystem:**
- **CVC-UAB** — Environment perception & computer vision
- **CAOS-UAB** — Embedded hardware & GPU optimization
- **UPC-Tarrasa** — Control & path planning
- **CTTC-UPC** — Positioning & localization
- **UAB-DEIC** — Vehicle-to-vehicle communications
- **UAB-CEPHIS** — Electronics & integration
- **CT Ingenieros** — Vehicle engineering & drive-by-wire
- **Municipality of Sant Quirze** — Test track facility

**Project Goals:**
Elektra serves as a **research and technology transfer hub** for intelligent mobility, combining cutting-edge academic research with real-world validation. The platform integrates multiple discipline areas—perception, planning, control, communications—to demonstrate production-ready autonomous driving in urban environments.

**Core Focus:**
The project heavily relies on **computer vision techniques** for high-level perception tasks (stereo vision, stixels, obstacle detection, scene understanding) while addressing the full stack: localization (GPS + IMU + vision), navigation (planning and control), and communications.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="project-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="elektra-car.png" alt="Elektra autonomous vehicle platform">
        </div>
        <div class="section-slideshow-image">
          <img src="overview.png" alt="Elektra team composition">
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

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('FWM-5Ps8zFo', 'Elektra Project Overview')">
      <img src="https://img.youtube.com/vi/FWM-5Ps8zFo/default.jpg" alt="Project Overview">
      <p>Project Overview</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('tvZnN65jbCE', 'Autonomous Driving Demo')">
      <img src="https://img.youtube.com/vi/tvZnN65jbCE/default.jpg" alt="Driving Demo">
      <p>Driving Demo</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('7u-mMtm1Q9o', 'Person Detection Demo')">
      <img src="https://img.youtube.com/vi/7u-mMtm1Q9o/default.jpg" alt="Person Detection">
      <p>Person Detection</p>
    </div>
  </div>
</div>

<script>initSlideshow('project', 2);</script>

---

## Computer Vision Center (CVC)

<div class="section-row reverse">
  <div class="section-text">

The **Computer Vision Center (CVC)** is a non-profit research institution founded in 1995 by the Generalitat de Catalunya and Universitat Autònoma de Barcelona. It has positioned itself as a reference in computer vision research through:

**Core Activities:**
- **Forming students** in Computer Vision, Machine Learning, AI, Real-time Systems, GPU Computing, and Autonomous Control
- **Basic research** producing high-impact papers in top-tier conferences and Q1 journals
- **Technological transfer & innovation** developing prototypes and products with industry partners
- **Dissemination** bringing research applications to the general public

The Elektra project exemplifies this mission—a **research platform with real-world impact** that drives both academic excellence and industry collaboration.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="cvc-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="image55.png" alt="CVC Research Facility">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'cvc')"></button>
        </div>
        <div class="slideshow-caption" id="cvc-caption">CVC Research Facility</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('FWM-5Ps8zFo', 'CVC Overview')">
      <img src="https://img.youtube.com/vi/FWM-5Ps8zFo/default.jpg" alt="CVC Overview">
      <p>CVC Overview</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('lVImNWXD5DE', 'Research Activities')">
      <img src="https://img.youtube.com/vi/lVImNWXD5DE/default.jpg" alt="Research">
      <p>Research Activities</p>
    </div>
  </div>
</div>

<script>initSlideshow('cvc', 1);</script>

---

## Perception System Design

<div class="section-row">
  <div class="section-text">

I **initiated and led the perception system development**, designing the full pipeline from raw sensor data to high-level scene understanding: object detection, semantic segmentation, 3D reconstruction, and SLAM.

The system integrates **multiple modalities** for robust environmental understanding:
- **Stereo cameras** for dense 3D reconstruction
- **Monocular vision** for long-range detection
- **LIDAR** for precise 3D mapping and obstacle detection
- **Inertial sensors** for motion estimation
- **Real-time GPU processing** for production-scale performance

**Key achievements:**
- Developed real-time 3D scene understanding pipelines
- Integrated multiple perception modalities for redundancy and accuracy
- Optimized GPU processing for embedded automotive hardware

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
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'perception')"></button>
          <button class="slideshow-dot" onclick="currentSlide(2, 'perception')"></button>
        </div>
        <div class="slideshow-caption" id="perception-caption">Real-time stereo vision processing</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('8TZx-FX2oaQ', 'Perception System')">
      <img src="https://img.youtube.com/vi/8TZx-FX2oaQ/default.jpg" alt="Perception System">
      <p>Perception System</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('UCWPV1eEy0w', 'Stixels')">
      <img src="https://img.youtube.com/vi/UCWPV1eEy0w/default.jpg" alt="Stixels">
      <p>Stixels</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('6dDNLvJVQjE', 'Real-time Processing')">
      <img src="https://img.youtube.com/vi/6dDNLvJVQjE/default.jpg" alt="Real-time Processing">
      <p>Real-time Processing</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('7u-mMtm1Q9o', 'Sensor Integration')">
      <img src="https://img.youtube.com/vi/7u-mMtm1Q9o/default.jpg" alt="Sensor Integration">
      <p>Sensor Integration</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('vDS7ZsZJKSU', 'Vision Pipeline')">
      <img src="https://img.youtube.com/vi/vDS7ZsZJKSU/default.jpg" alt="Vision Pipeline">
      <p>Vision Pipeline</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('_GRo6AyL3YQ', 'GPU Processing')">
      <img src="https://img.youtube.com/vi/_GRo6AyL3YQ/default.jpg" alt="GPU Processing">
      <p>GPU Processing</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('gs2XyPxKkpU', 'Embedded Systems')">
      <img src="https://img.youtube.com/vi/gs2XyPxKkpU/default.jpg" alt="Embedded Systems">
      <p>Embedded Systems</p>
    </div>
  </div>
</div>

<script>initSlideshow('perception', 2);</script>

---

## Obstacle & Pedestrian Detection

<div class="section-row reverse">
  <div class="section-text">

**Accurate pedestrian and obstacle detection** is the first critical capability for safe autonomous driving. The system must identify all potential hazards in real-time, from dynamic pedestrians to static obstacles.

**Detection capabilities:**
- **Real-time pedestrian detection** using convolutional neural networks
- **Multi-scale object detection** for obstacles at various distances
- **Temporal consistency** across frames to reduce false positives
- **Confidence scoring** for risk-aware planning decisions

**Key innovations:**
- GPU-accelerated detection pipelines (400+ FPS)
- Robust detection in diverse lighting and weather conditions
- Integration with planning for collision avoidance

The detection system feeds directly into the motion planning module, ensuring the vehicle can react to dynamic scenes in real-time.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="obstacle-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="image104.png" alt="Real-time pedestrian detection visualization">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'obstacle')"></button>
        </div>
        <div class="slideshow-caption" id="obstacle-caption">Real-time pedestrian detection visualization</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('7dYoVdYiG_8', 'Obstacle Detection')">
      <img src="https://img.youtube.com/vi/7dYoVdYiG_8/default.jpg" alt="Obstacle Detection">
      <p>Obstacle Detection</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('3mM0rq0pQ5c', 'Pedestrian Detection')">
      <img src="https://img.youtube.com/vi/3mM0rq0pQ5c/default.jpg" alt="Pedestrian Detection">
      <p>Pedestrian Detection</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('24wSDvo4SO4', 'Real-time Detection')">
      <img src="https://img.youtube.com/vi/24wSDvo4SO4/default.jpg" alt="Real-time Detection">
      <p>Real-time Detection</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('bO3ZwK3vVOM', 'Safety Systems')">
      <img src="https://img.youtube.com/vi/bO3ZwK3vVOM/default.jpg" alt="Safety Systems">
      <p>Safety Systems</p>
    </div>
  </div>
</div>

<script>initSlideshow('obstacle', 1);</script>

---

## Free Space & Lane Detection

<div class="section-row">
  <div class="section-text">

**Free space and lane detection** identifies drivable areas and lane boundaries, forming the second critical capability for safe navigation. The system distinguishes between obstacles and navigable space, and maintains lane awareness.

**Key components:**
- **Stixel representation** for efficient 3D scene geometry
- **Lane boundary detection** using road markings and structure
- **Drivable space segmentation** accounting for obstacles and curbs
- **Real-time processing** at full frame rate

**Technical approach:**
- Dense stereo processing for 3D depth
- Dynamic programming for optimal path detection
- Adaptive thresholding for varying road conditions
- Integration with localization for global path coherence

The free space representation enables the planning module to compute safe trajectories that avoid obstacles while staying within lane boundaries.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="freespace-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="image97.png" alt="Free-space detection highlighting drivable areas">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'freespace')"></button>
        </div>
        <div class="slideshow-caption" id="freespace-caption">Free-space detection highlighting drivable areas</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('K-rz32bW9l8', 'Free Space Detection')">
      <img src="https://img.youtube.com/vi/K-rz32bW9l8/default.jpg" alt="Free Space">
      <p>Free Space Detection</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('tBCPBHLrqcs', 'Lane Detection')">
      <img src="https://img.youtube.com/vi/tBCPBHLrqcs/default.jpg" alt="Lane Detection">
      <p>Lane Detection</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('2pDNvDN1x5M', 'Navigation Processing')">
      <img src="https://img.youtube.com/vi/2pDNvDN1x5M/default.jpg" alt="Navigation">
      <p>Navigation Processing</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('66RPhbhUTRY', 'Road Understanding')">
      <img src="https://img.youtube.com/vi/66RPhbhUTRY/default.jpg" alt="Road Understanding">
      <p>Road Understanding</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('6Yjd3XcHeVY', 'Drivable Space')">
      <img src="https://img.youtube.com/vi/6Yjd3XcHeVY/default.jpg" alt="Drivable Space">
      <p>Drivable Space</p>
    </div>
  </div>
</div>

<script>initSlideshow('freespace', 1);</script>

---

## SYNTHIA: Synthetic Data Innovation

<div class="section-row reverse">
  <div class="section-text">

**SYNTHIA** is a synthetic data generation framework that creates diverse, photorealistic driving scenarios for training and validation. This addresses the fundamental challenge: collecting large-scale, labeled data for autonomous driving is expensive and time-consuming.

**SYNTHIA capabilities:**
- **Multiple environmental conditions**: day, night, rain, fog, snow
- **Diverse urban scenarios**: intersections, pedestrian crossings, parked vehicles
- **Automatic labeling**: ground truth for semantic segmentation, depth, optical flow
- **Scalable generation**: thousands of labeled frames in hours

**Research impact:**
- Enables training robust perception models
- Provides controlled testing scenarios for algorithm validation
- Reduces dependency on expensive field data collection
- Published at top-tier conferences (CVPR, ICCV, ECCV)

SYNTHIA data powered much of the Elektra perception pipeline, ensuring robustness across diverse real-world conditions.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="synthia-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="synthia-360.png" alt="SYNTHIA daytime urban scenario">
        </div>
        <div class="section-slideshow-image">
          <img src="synthia-overview.png" alt="SYNTHIA nighttime driving">
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

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('qWJ6o_6XxQA', 'SYNTHIA Overview')">
      <img src="https://img.youtube.com/vi/qWJ6o_6XxQA/default.jpg" alt="SYNTHIA Overview">
      <p>SYNTHIA Overview</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('v1d8PiPt7EI', 'Synthetic Data Generation')">
      <img src="https://img.youtube.com/vi/v1d8PiPt7EI/default.jpg" alt="Synthetic Data">
      <p>Synthetic Data</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('N1-9a98YN8M', 'SYNTHIA Training')">
      <img src="https://img.youtube.com/vi/N1-9a98YN8M/default.jpg" alt="SYNTHIA Training">
      <p>SYNTHIA Training</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('HDNDKsOb6RE', 'Data Labeling')">
      <img src="https://img.youtube.com/vi/HDNDKsOb6RE/default.jpg" alt="Data Labeling">
      <p>Data Labeling</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('fQgw9ZA2loI', 'Rendering Engine')">
      <img src="https://img.youtube.com/vi/fQgw9ZA2loI/default.jpg" alt="Rendering Engine">
      <p>Rendering Engine</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('GCxm9TEGQOM', 'Urban Scenarios')">
      <img src="https://img.youtube.com/vi/GCxm9TEGQOM/default.jpg" alt="Urban Scenarios">
      <p>Urban Scenarios</p>
    </div>
  </div>
</div>

<script>initSlideshow('synthia', 2);</script>

---

## Localization & Positioning

<div class="section-row">
  <div class="section-text">

**Accurate localization** is critical—the vehicle must know its precise position relative to global maps and local obstacles. Elektra integrates multiple modalities for robust 6-DOF pose estimation.

**Localization approaches:**
- **GPS + IMU fusion** for global positioning with inertial smoothing
- **Visual odometry** from stereo cameras for local motion estimation
- **Loop closure detection** to correct drift over long distances
- **Semantic SLAM** leveraging detected landmarks

**Key challenges addressed:**
- GPS denial in urban canyons (bridges, tunnels)
- Sensor drift accumulation over long drives
- Real-time processing constraints for embedded hardware
- Robustness to dynamic scenes and moving objects

The localization module feeds global coordinates to the planning system, enabling precise navigation to destinations while integrating with local perception for immediate obstacle avoidance.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="localization-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="image95.png" alt="GPS and vision-based localization">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'localization')"></button>
        </div>
        <div class="slideshow-caption" id="localization-caption">GPS and vision-based localization</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('FY5rG5Pk6uE', 'Localization')">
      <img src="https://img.youtube.com/vi/FY5rG5Pk6uE/default.jpg" alt="Localization">
      <p>Localization</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('LRxmvkqpd8E', 'SLAM')">
      <img src="https://img.youtube.com/vi/LRxmvkqpd8E/default.jpg" alt="SLAM">
      <p>SLAM</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('aJxh8VGlwDg', 'GPS Integration')">
      <img src="https://img.youtube.com/vi/aJxh8VGlwDg/default.jpg" alt="GPS Integration">
      <p>GPS Integration</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('EnBKkxBm3bo', 'Map Matching')">
      <img src="https://img.youtube.com/vi/EnBKkxBm3bo/default.jpg" alt="Map Matching">
      <p>Map Matching</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('BH9QlZYv8oY', 'Sensor Fusion')">
      <img src="https://img.youtube.com/vi/BH9QlZYv8oY/default.jpg" alt="Sensor Fusion">
      <p>Sensor Fusion</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('umyqz35DahM', 'Position Estimation')">
      <img src="https://img.youtube.com/vi/umyqz35DahM/default.jpg" alt="Position Estimation">
      <p>Position Estimation</p>
    </div>
  </div>
</div>

<script>initSlideshow('localization', 1);</script>

---

## Path Planning & Navigation

<div class="section-row reverse">
  <div class="section-text">

**Motion planning** computes smooth, collision-free trajectories from the vehicle's current position to its destination. The planner integrates global route planning with local obstacle avoidance.

**Planning stack:**
- **Global planning** using road networks and maps to compute coarse routes
- **Local planning** generating smooth trajectories that respect vehicle dynamics
- **Trajectory optimization** minimizing time, fuel, and passenger comfort metrics
- **Reachability analysis** ensuring planned motions are executable by the vehicle

**Key innovations:**
- Real-time dynamic replanning as obstacles and goals change
- Integration with free-space and localization modules
- Consideration of vehicle kinematic constraints
- Safety-critical validation for automated motion

The planning module outputs reference trajectories that feed into the low-level vehicle control system, ensuring the vehicle executes safe, comfortable driving behaviors.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="planning-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="image73.png" alt="Path planning and trajectory visualization">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'planning')"></button>
        </div>
        <div class="slideshow-caption" id="planning-caption">Path planning and trajectory visualization</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('KWVkT1oMzHc', 'Path Planning')">
      <img src="https://img.youtube.com/vi/KWVkT1oMzHc/default.jpg" alt="Path Planning">
      <p>Path Planning</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('K-rz32bW9l8', 'Navigation')">
      <img src="https://img.youtube.com/vi/K-rz32bW9l8/default.jpg" alt="Navigation">
      <p>Navigation</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('jFYglohszXk', 'Trajectory Optimization')">
      <img src="https://img.youtube.com/vi/jFYglohszXk/default.jpg" alt="Trajectory">
      <p>Trajectory Optimization</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('I0hJxby__c8', 'Route Planning')">
      <img src="https://img.youtube.com/vi/I0hJxby__c8/default.jpg" alt="Route Planning">
      <p>Route Planning</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('jP42VX2uvPY', 'Obstacle Avoidance')">
      <img src="https://img.youtube.com/vi/jP42VX2uvPY/default.jpg" alt="Avoidance">
      <p>Obstacle Avoidance</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('L5auVNuYw7A', 'Dynamic Planning')">
      <img src="https://img.youtube.com/vi/L5auVNuYw7A/default.jpg" alt="Dynamic Planning">
      <p>Dynamic Planning</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('w2xadeEWLAo', 'Behavior Planning')">
      <img src="https://img.youtube.com/vi/w2xadeEWLAo/default.jpg" alt="Behavior Planning">
      <p>Behavior Planning</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('zIVRqvysEPw', 'Motion Strategies')">
      <img src="https://img.youtube.com/vi/zIVRqvysEPw/default.jpg" alt="Motion Strategies">
      <p>Motion Strategies</p>
    </div>
  </div>
</div>

<script>initSlideshow('planning', 1);</script>

---

## Vehicle Control & Execution

<div class="section-row">
  <div class="section-text">

**Low-level vehicle control** executes the planned trajectories by commanding steering, acceleration, and braking. This module transforms high-level motion plans into real-time actuator commands.

**Control architecture:**
- **Trajectory tracking control** maintaining planned position and velocity
- **Steering control** with constraints on maximum steering angle and rate
- **Longitudinal control** (acceleration/braking) respecting vehicle dynamics
- **Actuator interfacing** with drive-by-wire systems

**Technical highlights:**
- PID-based and model predictive control approaches
- Real-time embedded implementation on vehicle hardware
- Safety monitors detecting control failures
- Graceful degradation modes for fault tolerance

The control module is the final link in the autonomous driving chain, transforming software decisions into physical vehicle motion while ensuring safety and passenger comfort.

  </div>
  <div class="section-media">
    <div class="section-slideshow" id="control-slideshow">
      <div class="section-slideshow-container">
        <div class="section-slideshow-image active">
          <img src="control.png" alt="Low-level motion control">
        </div>
        <div class="section-slideshow-image">
          <img src="Electronics.png" alt="Vehicle actuator integration">
        </div>
        <div class="slideshow-nav">
          <button class="slideshow-dot active" onclick="currentSlide(1, 'control')"></button>
          <button class="slideshow-dot" onclick="currentSlide(2, 'control')"></button>
        </div>
        <div class="slideshow-caption" id="control-caption">Low-level motion control</div>
      </div>
    </div>
  </div>
</div>

<div class="section-video-carousel">
  <h4>Related Videos</h4>
  <div class="section-carousel-thumbnails">
    <div class="section-video-thumb" onclick="openVideoModal('PSpKVMXfNVE', 'Vehicle Control')">
      <img src="https://img.youtube.com/vi/PSpKVMXfNVE/default.jpg" alt="Vehicle Control">
      <p>Vehicle Control</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('fI_yKn3pN34', 'Drive-by-Wire')">
      <img src="https://img.youtube.com/vi/fI_yKn3pN34/default.jpg" alt="Drive-by-Wire">
      <p>Drive-by-Wire</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('tvZnN65jbCE', 'Integrated Control Demo')">
      <img src="https://img.youtube.com/vi/tvZnN65jbCE/default.jpg" alt="Control Demo">
      <p>Control Demo</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('sLq-o7mVl-M', 'Steering Control')">
      <img src="https://img.youtube.com/vi/sLq-o7mVl-M/default.jpg" alt="Steering">
      <p>Steering Control</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('OqNDF4LnKFY', 'Speed Control')">
      <img src="https://img.youtube.com/vi/OqNDF4LnKFY/default.jpg" alt="Speed Control">
      <p>Speed Control</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('OGZ5hMjlg0k', 'Safety Systems')">
      <img src="https://img.youtube.com/vi/OGZ5hMjlg0k/default.jpg" alt="Safety Systems">
      <p>Safety Systems</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('RqSYT5ZmwHI', 'Hardware Integration')">
      <img src="https://img.youtube.com/vi/RqSYT5ZmwHI/default.jpg" alt="Hardware Integration">
      <p>Hardware Integration</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('CB4384w4cgQ', 'Testing Procedures')">
      <img src="https://img.youtube.com/vi/CB4384w4cgQ/default.jpg" alt="Testing">
      <p>Testing Procedures</p>
    </div>
    <div class="section-video-thumb" onclick="openVideoModal('FfdSn_7b4s0', 'Real-world Validation')">
      <img src="https://img.youtube.com/vi/FfdSn_7b4s0/default.jpg" alt="Validation">
      <p>Real-world Validation</p>
    </div>
  </div>
</div>

<script>initSlideshow('control', 2);</script>

---

## Test Track & Controlled Environment

**Real-world validation** at the Sant Quirze test track and urban environments was essential for proving the integrated system. Controlled testing grounds allowed for systematic evaluation before public road operation.

**Testing program:**
- **Structured scenarios** with known obstacles and traffic patterns
- **Sensor characterization** under diverse weather and lighting conditions
- **Safety case building** documenting system reliability and failure modes
- **Public demonstrations** showcasing autonomous capabilities

The test track served as the primary venue for validating each subsystem—perception, planning, and control—both in isolation and as an integrated autonomous driving platform.

---

## Partnerships & Collaborators

The **multidisciplinary nature** of Elektra required collaboration across academic institutions and industry partners:

- **Universitat Autònoma de Barcelona (UAB)** — CVC (perception), CAOS (hardware), DEIC (communications), CEPHIS (electronics)
- **Universitat Politècnica de Catalunya (UPC)** — Tarrasa (control & planning), CTTC (positioning)
- **CT Ingenieros** — Vehicle engineering and drive-by-wire integration
- **Municipality of Sant Quirze** — Test track facility and urban testing permissions

This consortium model enabled knowledge transfer, technology validation, and real-world deployment—positioning Elektra as a complete autonomous driving platform rather than isolated research components.

---

## Key Publications

The Elektra project generated more than **20 peer-reviewed publications** at top-tier conferences and journals, including:

- **CVPR, ICCV, ECCV** — Computer vision and perception
- **IEEE TITS** — Intelligent transportation systems
- **IEEE T-IV** — Intelligent vehicles
- **Robotics and Autonomous Systems** — System integration and control

Key contributions include stixel-based 3D scene understanding, synthetic data generation (SYNTHIA), semantic segmentation for autonomous driving, and real-time perception system design.

---

## Legacy & Impact

**Elektra has left a lasting mark on autonomous driving research:**

- **Proof of concept** that vision-centric autonomous driving is achievable
- **Benchmark datasets** enabling community-wide algorithm comparison
- **Technology transfer** to industry and other research groups
- **Student training** producing graduates who advanced the field

The platform demonstrated that **accurate perception, robust planning, and reliable control** together enable urban autonomous driving—a paradigm that continues to influence modern autonomous vehicle development today.
