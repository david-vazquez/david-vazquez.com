---
title: Elektra Autonomous Vehicle
type: page
show_toc: false
reading_time: false
share: false
pager: false
date: '2014-01-01'
image:
  preview_only: true
links:
  - type: site
    url: 'https://adas.cvc.uab.es/elektra/'
    label: Project Website
---

<style>
.ek-hero{position:relative;width:100vw;margin-left:calc(-50vw + 50%);min-height:480px;display:flex;align-items:center;justify-content:center;overflow:hidden;background:#111}
.ek-hero-bg{position:absolute;inset:0;background-image:url('/media/elektra/elektra.png');background-size:cover;background-position:center;opacity:.45}
.ek-hero-content{position:relative;z-index:2;color:#fff;padding:4rem 2rem;max-width:820px;text-align:center}
.ek-hero-title{font-size:clamp(3rem,8vw,5rem);font-weight:800;letter-spacing:-.02em;margin:0;line-height:1;color:#fff}
.ek-hero-tagline{font-size:clamp(1rem,2.5vw,1.35rem);margin:1.25rem 0 0;opacity:.9;font-weight:400;color:rgba(255,255,255,.9)}
.ek-hero-text{font-size:.97rem;margin:1.5rem auto 2rem;line-height:1.75;opacity:.85;max-width:680px;text-align:left;color:rgba(255,255,255,.85)}
.ek-hero-actions{display:flex;flex-wrap:wrap;gap:1rem;justify-content:center}
.ek-btn-primary{display:inline-flex;align-items:center;gap:.5rem;padding:.875rem 1.75rem;background:rgb(var(--color-primary-600,37 99 235));color:#fff;border-radius:8px;cursor:pointer;font-size:1rem;font-weight:600;border:none;font-family:inherit;transition:background .2s,transform .1s;text-decoration:none}
.ek-btn-primary:hover{background:rgb(var(--color-primary-700,29 78 216));transform:translateY(-1px);color:#fff}
.ek-btn-secondary{display:inline-flex;align-items:center;gap:.5rem;padding:.875rem 1.5rem;background:rgba(255,255,255,.12);color:#fff;border-radius:8px;font-size:1rem;font-weight:500;border:1px solid rgba(255,255,255,.3);font-family:inherit;transition:background .2s;text-decoration:none}
.ek-btn-secondary:hover{background:rgba(255,255,255,.22);color:#fff}

.ek-div{border:none;border-top:1px solid rgba(0,0,0,.08);margin:3.5rem 0}
.dark .ek-div{border-top-color:rgba(255,255,255,.08)}

.ek-section{margin:0 0 1rem}
.ek-row{display:flex;gap:3rem;align-items:flex-start;margin-bottom:2.5rem}
.ek-row--img-right{flex-direction:row}
.ek-row--img-left{flex-direction:row-reverse}
.ek-text-col{flex:1;min-width:0}
.ek-img-col{flex:0 0 44%;min-width:0}
@media(max-width:768px){.ek-row,.ek-row--img-left,.ek-row--img-right{flex-direction:column}.ek-img-col{flex:1 1 100%}}

.ek-h2{font-size:1.75rem;font-weight:700;margin:0 0 1.25rem;line-height:1.2}

.ek-imgcar{border-radius:10px;overflow:hidden;background:#f0f0f0}
.dark .ek-imgcar{background:#222}
.ek-imgcar-track{display:flex;transition:transform .45s ease}
.ek-imgcar-slide{flex:0 0 100%;aspect-ratio:4/3;background:#f0f0f0}
.dark .ek-imgcar-slide{background:#222}
.ek-imgcar-slide img{width:100%;height:100%;object-fit:contain;display:block}
.ek-imgcar-nav{display:flex;justify-content:space-between;align-items:center;padding:.55rem .75rem;background:rgba(0,0,0,.04)}
.dark .ek-imgcar-nav{background:rgba(255,255,255,.04)}
.ek-imgcar-dots{display:flex;gap:6px}
.ek-imgcar-dot{width:8px;height:8px;border-radius:50%;background:rgba(0,0,0,.18);border:none;cursor:pointer;padding:0;transition:background .2s}
.dark .ek-imgcar-dot{background:rgba(255,255,255,.2)}
.ek-imgcar-dot.on{background:rgb(var(--color-primary-600,37 99 235))}
.dark .ek-imgcar-dot.on{background:rgb(var(--color-primary-400,96 165 250))}
.ek-imgcar-arr{background:none;border:none;cursor:pointer;font-size:1.1rem;color:#666;padding:.2rem .4rem;transition:color .2s}
.dark .ek-imgcar-arr{color:#aaa}
.ek-imgcar-arr:hover{color:rgb(var(--color-primary-600,37 99 235))}
.ek-single-img{border-radius:10px;overflow:hidden;aspect-ratio:4/3;background:#f0f0f0}
.dark .ek-single-img{background:#222}
.ek-single-img img{width:100%;height:100%;object-fit:contain;display:block}

.ek-vc-wrap{margin-top:1.75rem}
.ek-vc-label{font-size:.75rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#888;margin-bottom:.75rem}
.ek-vc{display:grid;grid-template-columns:2rem 1fr 2rem;gap:.5rem;align-items:center}
.ek-vc-btn{background:rgba(0,0,0,.06);border:none;border-radius:50%;width:2rem;height:2rem;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:background .2s;color:inherit;flex-shrink:0}
.dark .ek-vc-btn{background:rgba(255,255,255,.08)}
.ek-vc-btn:hover{background:rgba(0,0,0,.12)}
.dark .ek-vc-btn:hover{background:rgba(255,255,255,.15)}
.ek-vc-btn:disabled{opacity:.25;cursor:default}
.ek-vc-vp{overflow-x:scroll;scrollbar-width:none;-ms-overflow-style:none;scroll-snap-type:x mandatory;scroll-behavior:smooth}
.ek-vc-vp::-webkit-scrollbar{display:none}
.ek-vc-track{display:flex;gap:1rem}
.ek-vcard{flex:0 0 calc(33.333% - .667rem);cursor:pointer;border-radius:8px;overflow:hidden;background:rgba(0,0,0,.03);border:1px solid rgba(0,0,0,.06);transition:box-shadow .2s,transform .15s;scroll-snap-align:start}
.dark .ek-vcard{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.08)}
.ek-vcard:hover{box-shadow:0 4px 16px rgba(0,0,0,.12);transform:translateY(-2px)}
.ek-vcard-thumb{position:relative;aspect-ratio:16/9;overflow:hidden;background:#000}
.ek-vcard-thumb img{width:100%;height:100%;object-fit:cover;display:block;opacity:.85;transition:opacity .2s}
.ek-vcard:hover .ek-vcard-thumb img{opacity:1}
.ek-vcard-play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:2rem;color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.5);transition:transform .15s}
.ek-vcard:hover .ek-vcard-play{transform:scale(1.15)}
.ek-vcard-title{padding:.5rem .65rem;font-size:.77rem;font-weight:500;line-height:1.35;color:#444}
.dark .ek-vcard-title{color:#ccc}
@media(max-width:640px){.ek-vcard{flex:0 0 100%}}
@media(min-width:641px) and (max-width:900px){.ek-vcard{flex:0 0 calc(50% - .5rem)}}

.ek-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:9999;align-items:center;justify-content:center;padding:1.5rem}
.ek-modal.open{display:flex}
.ek-modal-box{background:#fff;border-radius:12px;max-width:880px;width:100%;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.4)}
.dark .ek-modal-box{background:#1a1a1a}
.ek-modal-hd{display:flex;justify-content:space-between;align-items:center;padding:.9rem 1.1rem;border-bottom:1px solid rgba(0,0,0,.1)}
.dark .ek-modal-hd{border-bottom-color:rgba(255,255,255,.1)}
.ek-modal-ttl{font-size:.95rem;font-weight:600;margin:0}
.ek-modal-x{background:none;border:none;font-size:1.4rem;cursor:pointer;color:#666;line-height:1;padding:.2rem .5rem}
.dark .ek-modal-x{color:#aaa}
.ek-modal-player{position:relative;padding-bottom:56.25%;height:0}
.ek-modal-player iframe{position:absolute;inset:0;width:100%;height:100%}
</style>

<div id="ek-modal" class="ek-modal" onclick="if(event.target===this)ekX()">
  <div class="ek-modal-box">
    <div class="ek-modal-hd">
      <span class="ek-modal-ttl" id="ek-ttl"></span>
      <button class="ek-modal-x" onclick="ekX()">✕</button>
    </div>
    <div class="ek-modal-player">
      <iframe id="ek-iframe" src="" frameborder="0" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>
    </div>
  </div>
</div>

<!-- HERO -->
<div class="ek-hero">
  <div class="ek-hero-bg"></div>
  <div class="ek-hero-content">
    <h1 class="ek-hero-title">Elektra</h1>
    <p class="ek-hero-tagline">A multidisciplinary autonomous driving research platform</p>
    <p class="ek-hero-text">Elektra is an autonomous driving research platform born at the Computer Vision Centre (CVC) at the Universitat Autònoma de Barcelona. I co-conceived and coordinated the project from the ground up: identifying the vehicle, leading the drive-by-wire transformation, assembling the consortium, and staying involved across every technical workstream. My primary expertise was perception, and the project was co-led with my supervisor Antonio López. Together we brought together more than 20 researchers across seven institutions, dozens of students, and industry partners including NVIDIA, who sponsored us with GPUs, cameras, and a DRIVE PX platform. Our embedded pedestrian detector won Best Poster at NVIDIA GTC 2016 in the USA. Elektra became the reference autonomous driving hub in Catalonia, attracting media coverage and becoming a landmark research project in the region.</p>
    <div class="ek-hero-actions">
      <button class="ek-btn-primary" onclick="ekV('tvZnN65jbCE','On-Road Demo')">▶ Watch the vehicle drive</button>
      <a class="ek-btn-secondary" href="https://www.youtube.com/playlist?list=PLOeT8nS-0X6AQQrui2AsgRKgz5zhdOFjl" target="_blank" rel="noopener">Full YouTube playlist →</a>
    </div>
  </div>
</div>

<hr class="ek-div" style="margin-top:3rem">

<!-- SECTION 2: OVERVIEW & CONSORTIUM — image LEFT -->
<div class="ek-section">
<div class="ek-row ek-row--img-left">
  <div class="ek-img-col">
    <div class="ek-single-img"><img src="/media/elektra/Elektra_team_overview.png" alt="Elektra team overview" loading="lazy"></div>
  </div>
  <div class="ek-text-col">
    <h2 class="ek-h2">Project Overview &amp; Consortium</h2>
    <p>Elektra was conceived as the Catalan hub for autonomous driving research, bringing together expertise from computer vision, embedded hardware, control theory, communications, electronics, and vehicle engineering under a single collaborative platform. The project aimed to bridge the gap between fundamental research and real-world intelligent mobility, with technology transfer as a core ambition.</p>
    <p>The consortium brought together seven institutions and the municipality of Sant Quirze del Vallès, which provided the test track and city environment for real-world validation. <strong>CVC/UAB</strong> led environment perception via computer vision; <strong>CAOS/UAB</strong> handled embedded hardware and high-performance computing on GPUs and FPGAs; <strong>UPC Terrassa</strong> developed control and planning; <strong>CTTC/UPC</strong> contributed positioning and sensor fusion (LIDAR, Radar, IMU, GNSS); <strong>UAB/DEIC</strong> covered vehicle communications (V2V and V2I); <strong>UAB/CEPHIS</strong> managed vehicle electronics and drive-by-wire; <strong>CT Ingenieros</strong> handled vehicle engineering, mechanics, and CAN bus; and the <strong>Ajuntament de Sant Quirze del Vallès</strong> provided the test track and city testing environment.</p>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 3: THE VEHICLE — image RIGHT -->
<div class="ek-section">
<div class="ek-row ek-row--img-right">
  <div class="ek-text-col">
    <h2 class="ek-h2">The Vehicle</h2>
    <p>Elektra is built on a Tazzari Zero electric microcar, chosen for its compact size, electric drivetrain, and suitability for urban driving research. One of the first and most critical steps of the project was transforming a standard production vehicle into a fully drive-by-wire platform: every actuator — throttle, steering, and brakes — was interfaced electronically so that a computer could issue commands directly over a CAN bus connection.</p>
    <p>The custom electronics board integrates a microprocessor, digital inputs and outputs, a steering sensor, accelerator DAC, brake control, noise reduction circuitry, and relay systems, giving the software stack full authority over the vehicle's motion while preserving manual override for safety.</p>
    <p>The vehicle was equipped with a purpose-built sensor and computing stack. Additional battery packs in the front trunk powered the onboard computers. A server in the rear trunk housed the GPUs, IMU, and GPS receiver. A roof-mounted rack carried a custom stereo camera pair and the GPS antenna, forming the primary sensing suite for perception and localization.</p>
    <p>For testing, Elektra had access to a dedicated track in Sant Quirze del Vallès, a scaled replica of the Catalonian Formula 1 circuit, providing a controlled environment for autonomous driving experiments before deployment on real urban streets in Barcelona.</p>
  </div>
  <div class="ek-img-col">
    <div class="ek-single-img"><img src="/media/elektra/Electronics.png" alt="Vehicle electronics" loading="lazy"></div>
  </div>
</div>
<div class="ek-vc-wrap">
  <div class="ek-vc-label">Videos</div>
  <div class="ek-vc" id="vc-vehicle">
    <button class="ek-vc-btn" onclick="ekVcP('vc-vehicle')">&#8592;</button>
    <div class="ek-vc-vp"><div class="ek-vc-track">
      <div class="ek-vcard" onclick="ekV('L5auVNuYw7A','Electronics and Drive-by-Wire')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/L5auVNuYw7A/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Electronics and Drive-by-Wire</div></div>
      <div class="ek-vcard" onclick="ekV('gs2XyPxKkpU','Test Track F1 Circuit Replica')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/gs2XyPxKkpU/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Test Track F1 Circuit Replica</div></div>
    </div></div>
    <button class="ek-vc-btn" onclick="ekVcN('vc-vehicle')">&#8594;</button>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 4: PERCEPTION — image LEFT -->
<div class="ek-section">
<div class="ek-row ek-row--img-left">
  <div class="ek-img-col">
    <div id="ic-perc" class="ek-imgcar">
      <div class="ek-imgcar-track">
        <div class="ek-imgcar-slide"><img src="/media/elektra/Perception1.png" alt="Perception overview" loading="lazy"></div>
        <div class="ek-imgcar-slide"><img src="/media/elektra/Perception_2.png" alt="Perception pipeline" loading="lazy"></div>
        <div class="ek-imgcar-slide"><img src="/media/elektra/GPU_FPGA_accelerated_algorithms.png" alt="GPU/FPGA algorithms" loading="lazy"></div>
      </div>
      <div class="ek-imgcar-nav">
        <button class="ek-imgcar-arr" onclick="ekIP('ic-perc')">&#8592;</button>
        <div class="ek-imgcar-dots">
          <button class="ek-imgcar-dot on" onclick="ekIG('ic-perc',0)"></button>
          <button class="ek-imgcar-dot" onclick="ekIG('ic-perc',1)"></button>
          <button class="ek-imgcar-dot" onclick="ekIG('ic-perc',2)"></button>
        </div>
        <button class="ek-imgcar-arr" onclick="ekIN('ic-perc')">&#8594;</button>
      </div>
    </div>
  </div>
  <div class="ek-text-col">
    <h2 class="ek-h2">Perception</h2>
    <p>Perception is the foundation of autonomous driving: the vehicle must understand its surroundings before it can make any decision. At Elektra, perception was the core expertise of the CVC team and the area where the project made its most significant research contributions.</p>
    <p>The primary sensing modality is a custom stereo camera pair, which provides dense 3D information about the driving scene. From this, we developed a full perception pipeline covering obstacle detection, free space estimation, semantic scene understanding, and driver monitoring.</p>
    <p>Obstacle and pedestrian detection was a central research thread, with detectors running on onboard cameras in urban Barcelona streets, from drone footage, and from train-mounted cameras. A pioneering result was our virtual world pedestrian detector presented at CVPR 2010, the first pedestrian detector trained entirely on video game imagery, foreshadowing the synthetic data revolution that would follow years later.</p>
    <p>Road and free space detection identifies the drivable area in real time using semantic segmentation, while traffic sign recognition detects and classifies road signs automatically. 3D scene understanding combines object detection, depth estimation from stereo, and semantic segmentation into a unified representation. The Stixels representation provides a compact and efficient obstacle map particularly suited for real-time processing.</p>
    <p>All of these algorithms were implemented to run at real-time speeds on embedded hardware. Using NVIDIA GPUs and FPGA boards, we achieved stereo depth at 100 FPS, Stixels at 400 FPS, and pedestrian detection at 100 FPS on the NVIDIA DRIVE PX platform. This work won Best Poster at NVIDIA GTC 2016 in the USA.</p>
    <p>ADAS features built on top of this perception stack include lane keeping assist, intelligent headlight control, and adaptive cruise control.</p>
  </div>
</div>
<div class="ek-vc-wrap">
  <div class="ek-vc-label">Videos</div>
  <div class="ek-vc" id="vc-perc">
    <button class="ek-vc-btn" onclick="ekVcP('vc-perc')">&#8592;</button>
    <div class="ek-vc-vp"><div class="ek-vc-track">
      <div class="ek-vcard" onclick="ekV('I0hJxby__c8','3D Scene Understanding')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/I0hJxby__c8/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">3D Scene Understanding</div></div>
      <div class="ek-vcard" onclick="ekV('7u-mMtm1Q9o','3D Stixels at 400 FPS')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/7u-mMtm1Q9o/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">3D Stixels at 400 FPS</div></div>
      <div class="ek-vcard" onclick="ekV('BH9QlZYv8oY','Person Detection from Car')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/BH9QlZYv8oY/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Person Detection from Car</div></div>
      <div class="ek-vcard" onclick="ekV('vDS7ZsZJKSU','Pedestrian Detection from Drone')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/vDS7ZsZJKSU/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Pedestrian Detection from Drone</div></div>
      <div class="ek-vcard" onclick="ekV('RqSYT5ZmwHI','Pedestrian Detection from Train')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/RqSYT5ZmwHI/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Pedestrian Detection from Train</div></div>
      <div class="ek-vcard" onclick="ekV('FfdSn_7b4s0','Road Detection')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/FfdSn_7b4s0/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Road Detection</div></div>
      <div class="ek-vcard" onclick="ekV('lVImNWXD5DE','Traffic Sign Detection')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/lVImNWXD5DE/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Traffic Sign Detection</div></div>
      <div class="ek-vcard" onclick="ekV('HDNDKsOb6RE','Virtual World Pedestrian Detection (CVPR 2010)')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/HDNDKsOb6RE/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Virtual World Pedestrian Detection</div></div>
      <div class="ek-vcard" onclick="ekV('zIVRqvysEPw','FPGA Stereo Computation')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/zIVRqvysEPw/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">FPGA Stereo Computation</div></div>
      <div class="ek-vcard" onclick="ekV('umyqz35DahM','GPU Pedestrian Detection at 100 FPS')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/umyqz35DahM/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">GPU Pedestrian Detection at 100 FPS</div></div>
      <div class="ek-vcard" onclick="ekV('OGZ5hMjlg0k','Lane Keeping')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/OGZ5hMjlg0k/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Lane Keeping</div></div>
      <div class="ek-vcard" onclick="ekV('OqNDF4LnKFY','Intelligent Lights Control')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/OqNDF4LnKFY/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Intelligent Lights Control</div></div>
      <div class="ek-vcard" onclick="ekV('24wSDvo4SO4','Adaptive Cruise Control')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/24wSDvo4SO4/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Adaptive Cruise Control</div></div>
    </div></div>
    <button class="ek-vc-btn" onclick="ekVcN('vc-perc')">&#8594;</button>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 5: LOCALIZATION — image RIGHT -->
<div class="ek-section">
<div class="ek-row ek-row--img-right">
  <div class="ek-text-col">
    <h2 class="ek-h2">Localization</h2>
    <p>For an autonomous vehicle to navigate safely, it must know precisely where it is at all times. Elektra's localization system fuses complementary sensing modalities to achieve robust and continuous position estimation in urban environments.</p>
    <p>The primary approach combines GPS and IMU data through sensor fusion, providing a global position reference with inertial corrections for smooth trajectory estimation. This is complemented by Visual Simultaneous Localization and Mapping (SLAM), which uses the onboard cameras to build a map of the environment while simultaneously tracking the vehicle's position within it, enabling localization even in areas where GPS signal is unreliable.</p>
    <p>Together these modalities give Elektra a robust sense of where it is, where it has been, and how to relate its perception outputs to a consistent world coordinate frame.</p>
  </div>
  <div class="ek-img-col">
    <div class="ek-single-img"><img src="/media/elektra/Perception_3.png" alt="Localization system" loading="lazy"></div>
  </div>
</div>
</div>
<div class="ek-vc-wrap">
  <div class="ek-vc-label">Videos</div>
  <div class="ek-vc" id="vc-loc">
    <button class="ek-vc-btn" onclick="ekVcP('vc-loc')">&#8592;</button>
    <div class="ek-vc-vp"><div class="ek-vc-track">
      <div class="ek-vcard" onclick="ekV('7g-jsv9sJW8','Visual SLAM')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/7g-jsv9sJW8/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Visual SLAM</div></div>
    </div></div>
    <button class="ek-vc-btn" onclick="ekVcN('vc-loc')">&#8594;</button>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 6: PLANNING & CONTROL — image LEFT -->
<div class="ek-section">
<div class="ek-row ek-row--img-left">
  <div class="ek-img-col">
    <div id="ic-ctrl" class="ek-imgcar">
      <div class="ek-imgcar-track">
        <div class="ek-imgcar-slide"><img src="/media/elektra/Control_and_planning.png" alt="Control and planning" loading="lazy"></div>
        <div class="ek-imgcar-slide"><img src="/media/elektra/Low_level_vehicle_control.png" alt="Low level vehicle control" loading="lazy"></div>
      </div>
      <div class="ek-imgcar-nav">
        <button class="ek-imgcar-arr" onclick="ekIP('ic-ctrl')">&#8592;</button>
        <div class="ek-imgcar-dots">
          <button class="ek-imgcar-dot on" onclick="ekIG('ic-ctrl',0)"></button>
          <button class="ek-imgcar-dot" onclick="ekIG('ic-ctrl',1)"></button>
        </div>
        <button class="ek-imgcar-arr" onclick="ekIN('ic-ctrl')">&#8594;</button>
      </div>
    </div>
  </div>
  <div class="ek-text-col">
    <h2 class="ek-h2">Planning &amp; Control</h2>
    <p>Once the vehicle knows its environment and its position within it, it must decide where to go and how to get there. Elektra's planning and control stack translates perception and localization outputs into smooth, safe vehicle motion.</p>
    <p>Global planning defines a route from point A to point B across the road network. Local planning operates at a finer scale, continuously adapting the trajectory to account for dynamic obstacles, road geometry, and traffic conditions detected by the perception system. Together they produce a motion plan that the low-level control layer then executes.</p>
    <p>The control interface provides direct electronic authority over throttle, steering, and braking via the CAN bus. A custom software dashboard allows engineers to monitor and tune every actuator in real time, including brake pressure, steering torque, acceleration curves, and speed profiles. Safety mechanisms such as the autonomous emergency braking system were validated extensively on the test track before any on-road deployment.</p>
    <p>The system was also used to demonstrate imitation learning, where the vehicle learned to drive by observing human driving behavior, and full end-to-end autonomous driving on real urban streets in Barcelona.</p>
  </div>
</div>
<div class="ek-vc-wrap">
  <div class="ek-vc-label">Videos</div>
  <div class="ek-vc" id="vc-ctrl">
    <button class="ek-vc-btn" onclick="ekVcP('vc-ctrl')">&#8592;</button>
    <div class="ek-vc-vp"><div class="ek-vc-track">
      <div class="ek-vcard" onclick="ekV('_GRo6AyL3YQ','Emergency Brake with Pedestrian')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/_GRo6AyL3YQ/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Emergency Brake with Pedestrian</div></div>
      <div class="ek-vcard" onclick="ekV('tvZnN65jbCE','On-Road Demo')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/tvZnN65jbCE/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">On-Road Demo</div></div>
      <div class="ek-vcard" onclick="ekV('bO3ZwK3vVOM','Imitation Learning')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/bO3ZwK3vVOM/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Imitation Learning</div></div>
      <div class="ek-vcard" onclick="ekV('6Yjd3XcHeVY','Learning in SYNTHIA Simulator')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/6Yjd3XcHeVY/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Learning in SYNTHIA Simulator</div></div>
    </div></div>
    <button class="ek-vc-btn" onclick="ekVcN('vc-ctrl')">&#8594;</button>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 7: SIMULATION — image RIGHT -->
<div class="ek-section">
<div class="ek-row ek-row--img-right">
  <div class="ek-text-col">
    <h2 class="ek-h2">Autonomous Driving Simulation</h2>
    <p>Training and testing autonomous driving algorithms on a real vehicle is expensive, slow, and carries safety risks. To overcome this, we developed SYNTHIA (SYNTHetic collection of Imagery and Annotations), a virtual urban environment purpose-built for autonomous driving research that became a major research contribution in its own right.</p>
    <p>SYNTHIA generates photo-realistic urban driving scenes with automatically produced ground truth annotations for every pixel: depth maps, semantic segmentation labels, and multi-camera views including 360-degree panoramas. Crucially, it covers a wide range of conditions including different times of day, weather (rain, snow, fog), and seasons, providing the diversity needed to train robust models.</p>
    <p>Within the Elektra project, SYNTHIA served as a safe and scalable sandbox for developing and validating the full autonomous driving stack. Perception algorithms were pre-trained on synthetic data before transfer to the real vehicle. Planning and control policies were tested in simulation before real-world deployment. This sim-to-real methodology significantly accelerated development and reduced risk during on-road testing.</p>
    <p>SYNTHIA was published at CVPR 2016 and has accumulated thousands of citations, becoming one of the most widely used synthetic datasets in the autonomous driving research community. See the <a href="/project/synthia/">SYNTHIA project page</a>.</p>
  </div>
  <div class="ek-img-col">
    <div id="ic-syn" class="ek-imgcar">
      <div class="ek-imgcar-track">
        <div class="ek-imgcar-slide"><img src="/media/elektra/Synthia_overview.png" alt="SYNTHIA overview" loading="lazy"></div>
        <div class="ek-imgcar-slide"><img src="/media/elektra/Synthia_360.png" alt="SYNTHIA 360" loading="lazy"></div>
      </div>
      <div class="ek-imgcar-nav">
        <button class="ek-imgcar-arr" onclick="ekIP('ic-syn')">&#8592;</button>
        <div class="ek-imgcar-dots">
          <button class="ek-imgcar-dot on" onclick="ekIG('ic-syn',0)"></button>
          <button class="ek-imgcar-dot" onclick="ekIG('ic-syn',1)"></button>
        </div>
        <button class="ek-imgcar-arr" onclick="ekIN('ic-syn')">&#8594;</button>
      </div>
    </div>
  </div>
</div>
<div class="ek-vc-wrap">
  <div class="ek-vc-label">Videos</div>
  <div class="ek-vc" id="vc-syn">
    <button class="ek-vc-btn" onclick="ekVcP('vc-syn')">&#8592;</button>
    <div class="ek-vc-vp"><div class="ek-vc-track">
      <div class="ek-vcard" onclick="ekV('w2xadeEWLAo','360 Camera Depth Map')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/w2xadeEWLAo/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">360 Camera Depth Map</div></div>
      <div class="ek-vcard" onclick="ekV('aJxh8VGlwDg','360 Degree Camera')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/aJxh8VGlwDg/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">360 Degree Camera</div></div>
      <div class="ek-vcard" onclick="ekV('66RPhbhUTRY','360 Semantic Segmentation')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/66RPhbhUTRY/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">360 Semantic Segmentation</div></div>
      <div class="ek-vcard" onclick="ekV('jP42VX2uvPY','Depth Maps')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/jP42VX2uvPY/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Depth Maps</div></div>
      <div class="ek-vcard" onclick="ekV('2pDNvDN1x5M','In the News')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/2pDNvDN1x5M/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">In the News</div></div>
      <div class="ek-vcard" onclick="ekV('fQgw9ZA2loI','Semantic Segmentation Ground Truth')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/fQgw9ZA2loI/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Semantic Segmentation Ground Truth</div></div>
      <div class="ek-vcard" onclick="ekV('EnBKkxBm3bo','Standard Camera View')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/EnBKkxBm3bo/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Standard Camera View</div></div>
      <div class="ek-vcard" onclick="ekV('GCxm9TEGQOM','Winter Conditions')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/GCxm9TEGQOM/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">Winter Conditions</div></div>
    </div></div>
    <button class="ek-vc-btn" onclick="ekVcN('vc-syn')">&#8594;</button>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 8: COMMUNICATIONS — image LEFT -->
<div class="ek-section">
<div class="ek-row ek-row--img-left">
  <div class="ek-img-col">
    <div class="ek-single-img"><img src="/media/elektra/Communications_for_intelligent_traffic_light_control.jpg" alt="Intelligent traffic light communications" loading="lazy"></div>
  </div>
  <div class="ek-text-col">
    <h2 class="ek-h2">Communications</h2>
    <p>Beyond the vehicle itself, Elektra explored how autonomous vehicles can interact with road infrastructure through Vehicle-to-Vehicle (V2V) and Vehicle-to-Infrastructure (V2I) communication protocols.</p>
    <p>The flagship demonstration of this workstream was an intelligent traffic light system. Camera-equipped traffic lights detect pedestrians and vehicles in their field of view and relay that information to a central Raspberry Pi controller, which adapts signal timing accordingly and broadcasts relevant information to approaching vehicles over a DTN (Delay-Tolerant Network) opportunistic contact protocol. This closed the loop between roadside perception and vehicle awareness, allowing Elektra to receive information about intersection conditions before even entering the junction.</p>
    <p>This work illustrated how smart infrastructure and autonomous vehicles can cooperate to improve safety and traffic flow, a direction that remains highly relevant to modern intelligent mobility research.</p>
  </div>
</div>
</div>

<hr class="ek-div">

<!-- SECTION 9: OUTREACH — image RIGHT -->
<div class="ek-section">
<div class="ek-row ek-row--img-right">
  <div class="ek-text-col">
    <h2 class="ek-h2">Outreach &amp; Publications</h2>
    <p>Elektra quickly became a reference project for autonomous driving research in Catalonia, attracting significant public interest and media attention. The vehicle was demonstrated at multiple public events, bringing autonomous driving technology directly to general audiences including families and school children. A particularly memorable outreach initiative saw high school students building their own autonomous driving system on a remote-control car, inspired by the Elektra platform and mentored by the CVC team.</p>
    <p>The project received substantial recognition from the research community and industry. NVIDIA sponsored the project with GPUs, cameras, and a DRIVE PX 2 platform, and our embedded pedestrian detector won Best Poster at NVIDIA GTC 2016 in the USA. The SYNTHIA dataset, published at CVPR 2016, went on to become one of the most cited synthetic datasets in autonomous driving research. Pedestrian detection work from the project traces back to CVPR 2010, one of the earliest demonstrations of training detectors on synthetic data.</p>
    <p>Over the course of the project the team produced a large body of peer-reviewed publications spanning perception, localization, planning, simulation, and embedded computing. A full list of publications is available on <a href="https://scholar.google.com/citations?user=pId0c6MAAAAJ" target="_blank" rel="noopener">Google Scholar</a>.</p>
  </div>
  <div class="ek-img-col">
    <div class="ek-single-img"><img src="/media/elektra/Demo_of_the_vehicle_in_an_event.jpg" alt="Vehicle demo at public event" loading="lazy"></div>
  </div>
</div>
<div class="ek-vc-wrap">
  <div class="ek-vc-label">Videos</div>
  <div class="ek-vc" id="vc-out">
    <button class="ek-vc-btn" onclick="ekVcP('vc-out')">&#8592;</button>
    <div class="ek-vc-vp"><div class="ek-vc-track">
      <div class="ek-vcard" onclick="ekV('jFYglohszXk','High School Autonomous RC Car Project')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/jFYglohszXk/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">High School Autonomous RC Car Project</div></div>
      <div class="ek-vcard" onclick="ekV('tvZnN65jbCE','On-Road Demo')"><div class="ek-vcard-thumb"><img src="https://img.youtube.com/vi/tvZnN65jbCE/hqdefault.jpg" alt="" loading="lazy"><div class="ek-vcard-play">▶</div></div><div class="ek-vcard-title">On-Road Demo</div></div>
    </div></div>
    <button class="ek-vc-btn" onclick="ekVcN('vc-out')">&#8594;</button>
  </div>
</div>
</div>

<script>
(function(){
var ii={};
function ekIG(id,n){var el=document.getElementById(id);if(!el)return;var s=el.querySelectorAll('.ek-imgcar-slide'),d=el.querySelectorAll('.ek-imgcar-dot');ii[id]=((n%s.length)+s.length)%s.length;el.querySelector('.ek-imgcar-track').style.transform='translateX(-'+(ii[id]*100)+'%)';d.forEach(function(x,i){x.classList.toggle('on',i===ii[id]);});}
function ekIN(id){ekIG(id,(ii[id]||0)+1);}
function ekIP(id){ekIG(id,(ii[id]||0)-1);}
window.ekIG=ekIG;window.ekIN=ekIN;window.ekIP=ekIP;

function ekVcP(id){var vp=document.querySelector('#'+id+' .ek-vc-vp'),c=vp.querySelector('.ek-vcard');if(c)vp.scrollBy({left:-(c.offsetWidth+16),behavior:'smooth'});}
function ekVcN(id){var vp=document.querySelector('#'+id+' .ek-vc-vp'),c=vp.querySelector('.ek-vcard');if(c)vp.scrollBy({left:c.offsetWidth+16,behavior:'smooth'});}
window.ekVcP=ekVcP;window.ekVcN=ekVcN;


function ekV(vid,title){document.getElementById('ek-ttl').textContent=title;document.getElementById('ek-iframe').src='https://www.youtube.com/embed/'+vid+'?autoplay=1';document.getElementById('ek-modal').classList.add('open');document.body.style.overflow='hidden';}
function ekX(){document.getElementById('ek-modal').classList.remove('open');document.getElementById('ek-iframe').src='';document.body.style.overflow='';}
window.ekV=ekV;window.ekX=ekX;
document.addEventListener('keydown',function(e){if(e.key==='Escape')ekX();});
})();
</script>
