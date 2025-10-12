```
---
sidebar_position: 5
---
```
# AFL Player Tracking & Crowd Monitoring System
## Complete Technical Documentation

---

**Document Version:** 1.0  
**Last Updated:** October 2025  
**Project:** Redback Operations - Project 4  
**Classification:** Technical Specification & Architecture Document

---

## 📋 Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [System Architecture](#2-system-architecture)
3. [Technology Stack](#3-technology-stack)
4. [Frontend Architecture](#4-frontend-architecture)
5. [Backend Architecture](#5-backend-architecture)
6. [Database Design](#6-database-design)
7. [AI/ML Components](#7-aiml-components)
8. [API Documentation](#8-api-documentation)
9. [Authentication & Security](#9-authentication--security)
10. [Core Features](#10-core-features)
11. [Data Flow & Processing](#11-data-flow--processing)
12. [Deployment Architecture](#12-deployment-architecture)
13. [Setup & Installation](#13-setup--installation)
14. [Performance & Optimization](#14-performance--optimization)
15. [Testing & Quality Assurance](#15-testing--quality-assurance)
16. [Future Enhancements](#16-future-enhancements)

---
## 1. Executive Summary

### 1.1 Project Overview

The **AFL Player Tracking and Crowd Monitoring System** is an advanced AI-powered platform designed to enhance safety, analytics, and performance insights during Australian Football League (AFL) matches. The system leverages state-of-the-art computer vision, deep learning, and real-time analytics through **two independent AI processing pipelines**:

1. ** Player Tracking Logic**: GPU-accelerated YOLOv11 and ByteTrack algorithms for multi-player detection, tracking, and performance analytics
2. ** Crowd Monitoring Logic**: Automated crowd density analysis and safety monitoring through person detection and heatmap generation usign LISA

Both pipelines integrate seamlessly through a unified dashboard, providing comprehensive monitoring capabilities for coaches, analysts, and stadium safety teams.

### 1.2 Key Objectives

**Player Tracking Pipeline Objectives:**
- **Multi-Player Detection**: Real-time detection and tracking of individual players using YOLOv11 and ByteTrack algorithms
- **Performance Analytics**: Distance traveled, speed metrics (avg/max), movement patterns, and intensity scores
- **Movement Heatmaps**: Individual player, team-wide, and zone-based (Back 50, Midfield, Forward 50) visualizations
- **Annotated Video**: Output videos with bounding boxes, player IDs, and tracking overlays
- **Strategic Insights**: CSV data export for advanced coaching analysis and tactical planning

**Crowd Monitoring Pipeline Objectives:**
- **Crowd Density Analysis**: Automated person detection and crowd concentration measurement
- **Safety Heatmaps**: Visual representation of crowd density for safety management
- **Spatial Distribution**: Frame-by-frame analysis of crowd movement and positioning
- **Alert Generation**: Real-time notifications for high-density areas and potential safety concerns
- **Capacity Monitoring**: People count tracking for stadium capacity management

**Shared System Objectives:**
- **Secure Access**: JWT-based authentication with OAuth integration (Google/Apple)
- **Unified Dashboard**: Single interface displaying both player and crowd analytics
- **Scalable Architecture**: Microservices design supporting independent pipeline scaling
- **Real-Time Processing**: Fast analysis with GPU acceleration and optimized algorithms

### 1.3 Business Value

**Player Tracking Benefits:**
- **Performance Optimization**: Data-driven training regimens based on distance, speed, and movement patterns
- **Injury Prevention**: Workload monitoring to prevent player fatigue and overexertion
- **Competitive Analysis**: Detailed movement analytics for tactical advantage
- **Coaching Efficiency**: Automated statistics reduce manual video analysis time by 80%
- **Player Development**: Track individual progress over time with historical data

**Crowd Monitoring Benefits:**
- **Enhanced Stadium Safety**: Real-time crowd density alerts prevent overcrowding incidents
- **Emergency Response**: Quick identification of problem areas for rapid intervention
- **Compliance**: Meet stadium capacity regulations and safety standards
- **Resource Optimization**: Efficient security and staff deployment based on crowd patterns
- **Revenue Protection**: Prevent crowd-related incidents that could lead to fines or closures

**Combined System Value:**
- **Holistic View**: Single platform for all match monitoring needs
- **Cost Efficiency**: Integrated solution reduces need for multiple separate systems
- **Data-Driven Decisions**: Comprehensive analytics for stakeholders across departments
- **Innovation Leadership**: Cutting-edge AI technology enhances organizational reputation

---

## 2. System Architecture

### 2.1 High-Level Architecture

The system follows a **microservices architecture** with three primary tiers and **two core AI processing pipelines**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT TIER                                     │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │              React 18 + Vite + TypeScript Frontend                     │  │
│  │   - Dashboard UI  - Auth UI  - Player Analytics  - Crowd Analytics    │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↕ HTTP/REST API
┌─────────────────────────────────────────────────────────────────────────────┐
│                           APPLICATION TIER                                   │
│                                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    Backend API Gateway (FastAPI)                     │    │
│  │                          Port 8000                                   │    │
│  │  - Authentication & JWT          - Video Upload Management           │    │
│  │  - User Authorization            - Analysis Orchestration            │    │
│  │  - Analytics Aggregation         - Static File Serving               │    │
│  └───────────────────┬──────────────────────────────┬──────────────────┘    │
│                      │                              │                        │
│                      ↓                              ↓                        │
│  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐│
│  │   PLAYER TRACKING LOGIC        │  │   CROWD MONITORING LOGIC       ││
│  ├──────────────────────────────────┤  ├──────────────────────────────────┤│
│  │ Tracking Microservice (FastAPI)  │  │ External Crowd API (ngrok)       ││
│  │ Port 8001 | GPU-Accelerated      │  │ External Service Integration     ││
│  ├──────────────────────────────────┤  ├──────────────────────────────────┤│
│  │  YOLOv11 Object Detection       │  │  Person Detection               ││
│  │  ByteTrack Multi-Object Tracking│  │  Crowd Density Analysis         ││
│  │  Player Speed & Distance Calc   │  │  Density Heatmap Generation     ││
│  │  Movement Heatmap Generation    │  │  People Count Per Frame         ││
│  │  Zone Analysis (Back 50, etc.)  │  │  Spatial Distribution Analysis  ││
│  │  Per-Player Analytics           │  │  Temporal Density Tracking      ││
│  │  Team-Wide Statistics           │  │  Frame-by-Frame Processing      ││
│  │  CSV & JSON Export              │  │  Safety Alert Generation        ││
│  └──────────────────────────────────┘  └──────────────────────────────────┘│
│              ↓                                      ↓                         │
│         Returns:                               Returns:                      │
│         - Tracked video                        - Heatmap images              │
│         - Player analytics JSON                - People count data           │
│         - Heatmap images                       - Frame snapshots             │
│         - CSV tracking data                    - Density metrics             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↕ SQL Queries
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DATA TIER                                       │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    PostgreSQL Database (Port 5432)                     │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │  Tables:                                                               │  │
│  │  • users             → User accounts & authentication                  │  │
│  │  • uploads           → Video file metadata                             │  │
│  │  • inferences        → Job tracking (player/crowd tasks)               │  │
│  │  • player_analysis   → Player tracking results & metrics               │  │
│  │  • crowd_analysis    → Crowd monitoring results & heatmaps             │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Components:**

1. **Player Tracking Logic** (Microservice on Port 8001)
   - GPU-accelerated YOLO-based detection
   - Real-time multi-object tracking
   - Movement analytics and heatmaps
   - Per-player and team statistics

2. **Crowd Monitoring Logic** (External API Integration)
   - Person detection in crowd scenes
   - Density heatmap generation
   - Safety monitoring capabilities
   - Frame sampling and analysis

### 2.2 Dual-Pipeline Architecture

The system implements **two independent AI processing pipelines** that can run simultaneously or separately:

**Pipeline 1: Player Tracking Logic** 
```
Video Input
    ↓
YOLOv11 Object Detection (GPU)
    ↓
ByteTrack Multi-Object Tracking
    ↓
Movement Path Extraction
    ↓
Speed & Distance Calculation
    ↓
Heatmap Generation (Individual + Team)
    ↓
Zone Analysis (Back 50, Midfield, Forward 50)
    ↓
Analytics JSON + CSV Export
```

**Pipeline 2: Crowd Monitoring Logic** 👥
```
Video Input
    ↓
Frame Sampling (Every 30th frame)
    ↓
Person Detection (External API)
    ↓
Crowd Density Analysis
    ↓
Heatmap Generation
    ↓
People Count Extraction
    ↓
Safety Metrics & Alerts
    ↓
Frame-by-Frame Storage
```

**Integration Benefits**:
- **Parallel Processing**: Both pipelines can run simultaneously on different videos
- **Independent Scaling**: Each pipeline scales based on its workload
- **Flexible Deployment**: Can be deployed together or separately
- **Unified Dashboard**: Both results displayed in single interface
- **Shared Infrastructure**: Common authentication, storage, and API gateway

### 2.3 Architecture Principles

- **Separation of Concerns**: Each service handles specific responsibilities
- **Dual-Pipeline Design**: Player tracking and crowd monitoring as independent modules
- **Scalability**: Independent microservices can scale horizontally
- **Resilience**: Service isolation prevents cascading failures
- **Modularity**: Components can be updated or replaced independently
- **Security by Design**: Authentication at every layer

### 2.4 Communication Patterns

**Frontend ↔ Backend Gateway**:
- **REST API**: Primary communication protocol
- **HTTP Multipart**: Video file uploads
- **JSON Payloads**: Structured data exchange
- **JWT Tokens**: Bearer token authentication
- **WebSocket** (Future): Real-time updates

**Backend Gateway ↔ Player Tracking Microservice**:
- **Internal HTTP/REST**: Service-to-service communication
- **Video File Transfer**: Multipart video upload
- **JSON Response**: Analytics and tracking data
- **Static URLs**: Links to heatmaps and processed videos

**Backend Gateway ↔ Crowd Monitoring API**:
- **External HTTP/REST**: Third-party API integration
- **Frame Upload**: Individual frame images (JPEG)
- **Image Response**: Heatmap PNG files
- **Custom Headers**: People count metadata

**Backend Gateway ↔ PostgreSQL Database**:
- **SQLAlchemy ORM**: Object-relational mapping
- **Connection Pooling**: Efficient database access
- **Transactions**: ACID compliance for data integrity

**Data Flow Summary**:
```
User Upload → Backend Gateway → {
    Player Tracking: Backend → Tracking Service → DB
    Crowd Monitoring: Backend → Crowd API → DB
} → Analytics Aggregation → Frontend Display
```

---

## 3. Technology Stack

### 3.1 Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.3.1 | UI framework for component-based development |
| **TypeScript** | 5.9.2 | Type-safe JavaScript for reduced runtime errors |
| **Vite** | 7.1.2 | Fast build tool and development server |
| **TailwindCSS** | 3.4.17 | Utility-first CSS framework |
| **React Router** | 6.30.1 | Client-side routing and navigation |
| **TanStack Query** | 5.84.2 | Server state management and caching |
| **Radix UI** | Various | Accessible component primitives |
| **Recharts** | 2.12.7 | Data visualization and charting |
| **Framer Motion** | 12.23.12 | Animation library |
| **Axios** | 1.12.2 | HTTP client with interceptors |
| **Zod** | 3.25.76 | Schema validation |
| **React Hook Form** | 7.62.0 | Form state management |

### 3.2 Backend Technologies

#### Main Backend Service (Port 8000)

| Technology | Version | Purpose |
|------------|---------|---------|
| **FastAPI** | 0.116.1 | High-performance async web framework |
| **Uvicorn** | 0.35.0 | ASGI server for FastAPI |
| **SQLAlchemy** | 2.0.43 | ORM for database operations |
| **PostgreSQL** | 15 | Relational database |
| **psycopg2-binary** | 2.9.10 | PostgreSQL adapter |
| **Alembic** | 1.13.2 | Database migration tool |
| **Pydantic** | 2.11.7 | Data validation |
| **PassLib** | 1.7.4 | Password hashing |
| **python-jose** | 3.5.0 | JWT token generation |
| **OpenCV** | 4.10.0.84 | Image processing |
| **NumPy** | 1.26.4 | Numerical computing |
| **Pandas** | 2.2.2 | Data manipulation |
| **Matplotlib** | 3.9.0 | Plotting and visualization |

#### Tracking Microservice (Port 8001)

| Technology | Version | Purpose |
|------------|---------|---------|
| **FastAPI** | 0.111.0 | API framework |
| **PyTorch** | 2.5.1+cu121 | Deep learning framework with CUDA |
| **Ultralytics** | 8.3.161 | YOLOv11 implementation |
| **OpenCV** | 4.10.0.84 | Video processing |
| **EasyOCR** | 1.7.2 | Optical character recognition |
| **SciPy** | 1.15.1 | Scientific computing |
| **scikit-image** | 0.25.2 | Image processing algorithms |

### 3.3 Infrastructure & DevOps

- **Docker**: Containerization (PostgreSQL container)
- **Git**: Version control
- **GitHub**: Repository hosting
- **VS Code**: Primary development environment
- **Google Colab**: Cloud GPU for model training
- **Jupyter Notebooks**: Experimentation and analysis

### 3.4 AI/ML Models

- **YOLOv11**: State-of-the-art object detection
- **ByteTrack**: Multi-object tracking algorithm
- **Custom AFL Player Model**: Fine-tuned on AFL footage
- **Gaussian Filtering**: Heatmap smoothing algorithm

---

## 4. Frontend Architecture

### 4.1 Project Structure

```
frontend/
├── client/
│   ├── pages/                    # Route-level components
│   │   ├── Index.tsx             # Landing page
│   │   ├── Login.tsx             # Authentication page
│   │   ├── AFLDashboard.tsx      # Main dashboard
│   │   ├── PlayerPerformance.tsx # Player analytics
│   │   ├── CrowdMonitor.tsx      # Crowd monitoring
│   │   ├── Analytics.tsx         # Advanced analytics
│   │   ├── Reports.tsx           # Report generation
│   │   └── TeamMatchPerformance.tsx
│   ├── components/
│   │   ├── auth/                 # Authentication components
│   │   ├── dashboard/            # Dashboard components
│   │   │   ├── tabs/             # Tab panels
│   │   │   ├── DashboardHeader.tsx
│   │   │   ├── PlayerStatsGrid.tsx
│   │   │   ├── VideoUploadPanel.tsx
│   │   │   └── ...
│   │   ├── ui/                   # Reusable UI primitives
│   │   ├── ErrorBoundary.tsx
│   │   └── ...
│   ├── hooks/                    # Custom React hooks
│   │   ├── useDashboardState.ts
│   │   ├── use-processing-queue.ts
│   │   └── use-oauth.ts
│   ├── lib/                      # Utility functions
│   │   ├── auth.ts
│   │   ├── video.ts
│   │   ├── crowd.ts
│   │   ├── reports.ts
│   │   ├── download.ts
│   │   └── utils.ts
│   ├── types/                    # TypeScript definitions
│   │   ├── api.ts
│   │   └── dashboard.ts
│   ├── api/
│   │   └── axiosInstance.ts      # Configured Axios client
│   ├── App.tsx                   # Root component & routing
│   ├── main.tsx                  # Application entry point
│   └── global.css                # Global styles
├── server/                       # Express server (OAuth)
│   ├── routes/
│   │   ├── oauth.ts
│   │   └── demo.ts
│   └── index.ts
├── shared/                       # Shared types (client & server)
│   ├── api.ts
│   └── oauth.ts
├── package.json
├── vite.config.ts
├── tailwind.config.ts
└── tsconfig.json
```

### 4.2 Routing Architecture

**React Router 6 Configuration** (SPA Mode):

```typescript
Routes:
  / → Login Page
  /login → Login Page
  /home → AFL Dashboard (authenticated)
  /afl-dashboard → AFL Dashboard
  /player-performance → Player Performance Analytics
  /crowd-monitor → Crowd Monitoring
  /analytics → Advanced Analytics
  /reports → Report Generation
  /team-match-performance → Team Comparison
  /api-diagnostics → System Diagnostics
  * → 404 Not Found
```

### 4.3 State Management Strategy

#### Global State (TanStack Query)
- Server data caching
- Automatic refetching
- Optimistic updates
- Error retry logic

#### Local State (useState/useReducer)
- UI state (modals, tabs, selections)
- Form state (React Hook Form)
- Dashboard state (custom hook)

#### Authentication State
- JWT token in localStorage
- User email in localStorage
- Axios interceptor for token injection
- Auto-redirect on 401 responses

### 4.4 Key Frontend Components

#### AFLDashboard Component
- **Purpose**: Main application interface
- **Features**: Tab-based navigation, video upload, analysis results
- **State**: Managed by `useDashboardState` hook
- **Tabs**: Video Analysis, Player Performance, Crowd Monitor, Reports

#### VideoUploadPanel Component
- Drag-and-drop file upload
- Progress tracking
- Analysis type selection (Player/Crowd)
- Queue management

#### PlayerStatsGrid Component
- Real-time player metrics
- Distance traveled
- Speed (avg/max)
- Heatmap visualization
- Zone activity analysis

### 4.5 API Integration Layer

**Axios Instance Configuration**:
```typescript
- Base URL: http://127.0.0.1:8000
- Request Interceptor: Inject JWT token
- Response Interceptor: Handle 401 → redirect to /login
- Timeout: 30 seconds
- Error handling: Centralized error mapping
```

---

## 5. Backend Architecture

### 5.1 Main Backend Service (Port 8000)

#### Service Structure

```
backend/
├── main.py                 # FastAPI application entry point
├── storage.py              # Database ORM models & helpers
├── routes/
│   ├── __init__.py
│   ├── auth.py             # Authentication endpoints
│   ├── upload.py           # Video upload handling
│   ├── inference.py        # Inference orchestration
│   ├── tracking_analysis_simple.py  # Tracking analytics
│   ├── crowd.py            # Crowd monitoring
│   ├── analysis.py         # Analysis retrieval
│   ├── metrics.py          # Metrics APIs
│   └── metrics_store.py    # Metrics storage
├── config/
│   └── cors.py             # CORS configuration
├── static/                 # Static file serving
│   ├── heatmaps/
│   ├── analytics/
│   └── crowd/
├── uploaded_videos/        # Video storage
├── requirements.txt
└── README.md
```

#### Core Responsibilities

1. **Authentication & Authorization**
   - User registration with bcrypt password hashing
   - JWT token generation and validation
   - OAuth integration (Google/Apple)
   - Role-based access control

2. **Video Management**
   - Multipart file upload handling
   - Unique UUID generation per upload
   - File path storage in PostgreSQL
   - Original filename preservation

3. **Inference Orchestration**
   - Player tracking service coordination
   - Crowd monitoring API integration
   - Job status tracking (Analyzing/Completed/Failed)
   - Result aggregation and storage

4. **Analytics Processing**
   - Heatmap localization (download from microservice)
   - JSON analytics storage
   - Per-player statistics calculation
   - Zone-based analysis (Back 50, Midfield, Forward 50)

5. **Static File Serving**
   - Annotated videos
   - Heatmap images
   - Analytics JSON
   - Crowd detection frames

### 5.2 Tracking Microservice (Port 8001)

#### Service Structure

```
tracking_code/
├── main.py               # FastAPI tracking service
├── track.py              # YOLO tracking implementation
├── afl_heatmap.py        # Heatmap generation pipeline
├── demo.py               # Standalone demo
├── best.pt               # YOLOv11 trained weights
├── uploads/              # Temporary video storage
├── outputs/              # Tracked videos & CSVs
├── analytics/            # JSON analytics
├── heatmaps/             # Generated heatmaps
│   ├── <label>/
│   │   ├── overall/      # Team-wide heatmap
│   │   ├── per_id/       # Individual player heatmaps
│   │   └── zones/        # Zone-specific heatmaps
├── requirements.txt
└── README.md
```

#### Core Responsibilities

1. **Video Processing**
   - Frame extraction using OpenCV
   - GPU-accelerated inference (CUDA 12.1)
   - FPS detection and timestamp calculation

2. **Player Detection**
   - YOLOv11 object detection
   - Confidence threshold filtering (default: 0.3)
   - Bounding box extraction
   - Overlap filtering (IOU-based)

3. **Multi-Object Tracking**
   - ByteTrack algorithm integration
   - Persistent ID assignment across frames
   - Track management and lifecycle

4. **Analytics Generation**
   - Distance calculation (pixel → meter conversion)
   - Speed metrics (average and maximum)
   - Movement path smoothing
   - CSV export for downstream processing

5. **Heatmap Pipeline**
   - AFL oval dimension scaling (159.5m × 128.8m)
   - Gaussian smoothing (configurable sigma)
   - Confidence-weighted intensity
   - Zone segmentation (circular regions)
   - Per-player and team-wide visualizations

### 5.3 API Gateway Pattern

The main backend acts as an API gateway:
- **Frontend ← Backend API**: RESTful endpoints
- **Backend API → Tracking Service**: Internal HTTP calls
- **Backend API → Crowd Service**: External ngrok API
- **Backend API → PostgreSQL**: Direct database access

---

## 6. Database Design

### 6.1 Table Definitions

#### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

**Purpose**: Store user accounts for authentication
**Indexes**: `email` (unique)

#### Uploads Table
```sql
CREATE TABLE uploads (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER REFERENCES users(id) NOT NULL,
    path VARCHAR(512) NOT NULL,
    media_type VARCHAR(32) DEFAULT 'video',
    size_bytes INTEGER DEFAULT 0,
    original_filename VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_uploads_user_id ON uploads(user_id);
```

**Purpose**: Track all video uploads
**Relationships**: N:1 with Users

#### Inferences Table
```sql
CREATE TABLE inferences (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER REFERENCES users(id) NOT NULL,
    upload_id UUID REFERENCES uploads(id) ON DELETE CASCADE,
    task VARCHAR(16) NOT NULL,  -- 'player' or 'crowd'
    status VARCHAR(16) DEFAULT 'ok',
    payload JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_inferences_upload_id ON inferences(upload_id);
CREATE INDEX idx_inferences_user_id ON inferences(user_id);
```

**Purpose**: Track analysis jobs and their status
**Cascade**: Deletes when parent upload is deleted
**Payload Examples**:
- Analyzing: `{}`
- Completed: `{files: {...}, analytics: {...}}`
- Failed: `{error: "..."}`

#### PlayerAnalysis Table
```sql
CREATE TABLE player_analysis (
    id SERIAL PRIMARY KEY,
    upload_id UUID REFERENCES uploads(id) NOT NULL,
    player_id INTEGER NOT NULL,
    json_path VARCHAR(512) NOT NULL,
    heatmap_path VARCHAR(512) NOT NULL,
    team_heatmap_path VARCHAR(512),
    zone_back_50_path VARCHAR(512),
    zone_midfield_path VARCHAR(512),
    zone_forward_50_path VARCHAR(512),
    stats JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_player_analysis_upload_id ON player_analysis(upload_id);
```

**Purpose**: Store per-player tracking analytics
**Stats JSONB Structure**:
```json
{
  "distance_m": 1234.56,
  "average_speed_m_s": 2.34,
  "average_speed_kmh": 8.42,
  "max_speed_m_s": 6.78,
  "max_speed_kmh": 24.41
}
```

#### CrowdAnalysis Table
```sql
CREATE TABLE crowd_analysis (
    id SERIAL PRIMARY KEY,
    upload_id UUID REFERENCES uploads(id) NOT NULL,
    frame_number INTEGER NOT NULL,
    people_count INTEGER,
    frame_image_path VARCHAR(512) NOT NULL,
    heatmap_image_path VARCHAR(512) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_crowd_analysis_upload_id ON crowd_analysis(upload_id);
```

**Purpose**: Store crowd density analysis per frame
**Sampling**: Every 30th frame for performance

### 6.2 Data Access Patterns

#### Storage Helper Functions

```python
# Upload management
save_upload(path, media_type, size_bytes, user_id, filename) → dict
get_upload(upload_id) → dict | None

# Inference tracking
save_inference(upload_id, user_id, task, status, payload) → dict
get_inferences(upload_id) → list[dict]

# Player analytics
save_player_analysis(upload_id, player_id, json_path, ...) → dict
get_player_analysis(upload_id, player_id) → dict | None

# Crowd analytics
save_crowd_analysis(upload_id, frame_number, people_count, ...) → dict
get_crowd_analysis(upload_id) → list[dict]
```

---

## 7. AI/ML Components

### 7.1 YOLOv11 Object Detection

**Model Architecture**: YOLOv11 (You Only Look Once v11)
- **Type**: Single-stage object detector
- **Backbone**: CSPDarknet
- **Head**: Detection head with anchor-free prediction
- **Input**: Variable resolution (typically 640×640)
- **Output**: Bounding boxes, class probabilities, confidence scores

**Model Training**:
- **Dataset**: Custom AFL player dataset
- **Training Platform**: Google Colab with GPU
- **Framework**: Ultralytics (PyTorch-based)
- **Weights**: `best.pt` (fine-tuned model)
- **Classes**: Single class ("player")

**Inference Configuration**:
```python
model = YOLO("best.pt")
results = model.track(
    frame,
    persist=True,
    tracker="bytetrack.yaml",
    conf=0.3,  # Confidence threshold
    device="cuda"  # GPU acceleration
)
```

### 7.2 ByteTrack Multi-Object Tracking

**Algorithm**: ByteTrack (modified SORT)
- **Method**: Kalman filtering + Hungarian algorithm
- **Features**:
  - Low-confidence detection recovery
  - Occlusion handling
  - ID persistence across frames
  - Fast association (real-time capable)

**Tracking Pipeline**:
1. **Detection**: YOLOv11 produces bounding boxes
2. **Prediction**: Kalman filter predicts next position
3. **Association**: Hungarian algorithm matches detections to tracks
4. **Update**: Track states updated with matched detections
5. **Management**: New tracks created, lost tracks removed

**Overlap Filtering**:
```python
def calculate_iou(box1, box2):
    # Intersection over Union
    intersection = calculate_intersection(box1, box2)
    union = area(box1) + area(box2) - intersection
    return intersection / union

# Keep only highest confidence when IoU > 0.7
```

### 7.3 Heatmap Generation Algorithm

**Mathematical Foundation**:

**1. Coordinate Transformation**:
```
Raw pixels → AFL oval metres
x_m = ((x - x_min) / (x_max - x_min)) * 159.5 - 79.75
y_m = ((y - y_min) / (y_max - y_min)) * 128.8 - 64.4
```

**2. Grid Discretization**:
- Resolution: 200×150 cells
- Coverage: Full AFL oval (159.5m × 128.8m)
- Cell size: ~0.8m × 0.86m

**3. Density Accumulation**:
```
H[i,j] += weight(confidence)
where (i,j) = grid cell containing (x_m, y_m)
```

**4. Gaussian Smoothing**:
```
H_smooth = gaussian_filter(H, sigma=2.0)
```

**5. Oval Masking**:
```
mask = (x²/a²) + (y²/b²) ≤ 1
where a=79.75m, b=64.4m (semi-axes)
```

**Zone Segmentation**:
- **Back 50**: Circular region (radius 50m) from left goal
- **Forward 50**: Circular region (radius 50m) from right goal
- **Midfield**: Remaining central area

### 7.4 Performance Metrics

**Player Analytics Calculations**:

```python
# Distance calculation
distance_m = Σ(euclidean_distance(pos[i], pos[i-1]) * 0.05)

# Speed calculation
speed_m_s = distance_m / (timestamp[i] - timestamp[i-1])

# Outlier rejection
if speed_m_s > 8.0:  # Unrealistic AFL speed
    reject()

# Smoothing
smoothed_pos = moving_average(positions, window=5)
```

**Crowd Density Metrics**:
- **People Count**: Number of detected persons per frame
- **Spatial Distribution**: Heatmap intensity values
- **Temporal Analysis**: Frame-by-frame density changes

### 7.5 GPU Acceleration

**CUDA Configuration**:
```
PyTorch: 2.5.1+cu121
CUDA Version: 12.1
cuDNN: Enabled
Device: NVIDIA GPU
Compute Capability: 7.0+
```

**Performance Impact**:
- **CPU-only**: ~5-10 FPS processing
- **GPU (CUDA)**: ~60-120 FPS processing
- **Speedup**: 10-20× faster inference

---

## 8. API Documentation

### 8.1 Authentication APIs

#### POST `/api/v1/auth/register`
**Description**: Create new user account

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Errors**:
- `400`: Email already registered
- `422`: Validation error

---

#### POST `/api/v1/auth/login`
**Description**: Authenticate user and receive JWT token

**Request Body** (Form Data):
```
username: user@example.com
password: securePassword123
```

**Response** (200 OK):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Errors**:
- `401`: Invalid credentials

---

### 8.2 Upload APIs

#### POST `/api/v1/uploads/video`
**Description**: Upload video file for analysis

**Headers**:
```
Authorization: Bearer <token>
Content-Type: multipart/form-data
```

**Request Body** (Form Data):
```
file: <video.mp4>
```

**Response** (200 OK):
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "user_id": 1,
  "path": "uploaded_videos/a1b2c3d4_video.mp4",
  "media_type": "video",
  "size_bytes": 15728640,
  "original_filename": "match_footage.mp4",
  "created_at": "2025-10-10T12:34:56Z"
}
```

**Errors**:
- `401`: Unauthorized
- `413`: File too large
- `415`: Unsupported media type

---

#### GET `/api/v1/uploads/list`
**Description**: List all uploads for authenticated user

**Headers**:
```
Authorization: Bearer <token>
```

**Response** (200 OK):
```json
[
  {
    "id": "a1b2c3d4-...",
    "original_filename": "match1.mp4",
    "created_at": "2025-10-10T12:34:56Z",
    "size_bytes": 15728640
  },
  ...
]
```

---

### 8.3 Inference APIs

#### POST `/api/v1/inference/player/track`
**Description**: Run player tracking analysis

**Headers**:
```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body**:
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "location": "Marvel Stadium",
  "sampling_fps": 5,
  "conf_threshold": 0.5
}
```

**Response** (200 OK):
```json
{
  "id": "a1b2c3d4-...",
  "task": "player-track",
  "status": "ok",
  "team_heatmap": "http://127.0.0.1:8000/static/heatmaps/.../team.png",
  "zones": {
    "back_50": "http://127.0.0.1:8000/static/heatmaps/.../zones/back_50.png",
    "midfield": "http://127.0.0.1:8000/static/heatmaps/.../zones/midfield.png",
    "forward_50": "http://127.0.0.1:8000/static/heatmaps/.../zones/forward_50.png"
  },
  "team_analytics_json": "http://127.0.0.1:8000/static/analytics/.../analytics.json",
  "data": {
    "video_info": {
      "duration": 30.5,
      "fps": 30,
      "total_frames": 915,
      "resolution": [1920, 1080]
    },
    "players": [
      {
        "id": 1,
        "distance_m": 234.56,
        "average_speed_m_s": 2.34,
        "average_speed_kmh": 8.42,
        "max_speed_m_s": 6.78,
        "max_speed_kmh": 24.41,
        "heatmap": "http://127.0.0.1:8000/static/heatmaps/.../players/id_1.png"
      },
      ...
    ]
  }
}
```

**Errors**:
- `401`: Unauthorized
- `403`: Not authorized to access this upload
- `404`: Upload not found
- `410`: File missing on disk
- `502`: Tracking service error
- `500`: Internal server error

---

#### POST `/api/v1/inference/crowd/{upload_id}`
**Description**: Run crowd monitoring analysis

**Headers**:
```
Authorization: Bearer <token>
```

**Response** (200 OK):
```json
{
  "status": "success",
  "upload_id": "a1b2c3d4-...",
  "inference": {
    "id": "b2c3d4e5-...",
    "status": "Completed",
    "task": "crowd"
  },
  "frames_analyzed": 30,
  "frames_detected": 25,
  "results": [
    {
      "frame_number": 0,
      "people_count": 42,
      "frame_image_path": "http://127.0.0.1:8000/static/crowd/.../frames/frame_0.jpg",
      "heatmap_image_path": "http://127.0.0.1:8000/static/crowd/.../heatmaps/heatmap_0.png"
    },
    ...
  ]
}
```

**Special Cases**:
- If no people detected: `status: "no-heatmaps"`
- Failed analysis: `status: "Failed"`

---

#### GET `/api/v1/inference/inferences?upload_id={id}`
**Description**: Get all inference jobs for an upload

**Headers**:
```
Authorization: Bearer <token>
```

**Response** (200 OK):
```json
[
  {
    "id": "inference-uuid",
    "upload_id": "upload-uuid",
    "user_id": 1,
    "task": "player",
    "status": "Completed",
    "payload": { ... },
    "created_at": "2025-10-10T12:34:56Z"
  },
  ...
]
```

---

### 8.4 Analysis APIs

#### GET `/api/v1/analysis/player/{upload_id}/player/{player_id}`
**Description**: Get specific player's analysis data

**Response** (200 OK):
```json
{
  "id": 123,
  "upload_id": "a1b2c3d4-...",
  "player_id": 1,
  "json_path": "http://127.0.0.1:8000/static/analytics/.../analytics.json",
  "heatmap_path": "http://127.0.0.1:8000/static/heatmaps/.../id_1.png",
  "team_heatmap_path": "http://127.0.0.1:8000/static/heatmaps/.../team.png",
  "zone_back_50_path": "http://...",
  "zone_midfield_path": "http://...",
  "zone_forward_50_path": "http://...",
  "stats": {
    "distance_m": 234.56,
    "average_speed_kmh": 8.42,
    "max_speed_kmh": 24.41
  }
}
```

---

#### GET `/api/v1/analysis/crowd/{upload_id}`
**Description**: Get all crowd analysis frames for a video

**Response** (200 OK):
```json
[
  {
    "frame_number": 0,
    "people_count": 42,
    "frame_image_path": "http://...",
    "heatmap_image_path": "http://..."
  },
  ...
]
```

---

### 8.5 Tracking Microservice APIs (Port 8001)

#### POST `/track`
**Description**: Process video with player tracking

**Request** (Multipart Form):
```
file: <video.mp4>
```

**Response** (200 OK):
```json
{
  "status": "success",
  "upload_id": "uuid",
  "files": {
    "input_video": "http://127.0.0.1:8001/uploads/uuid_video.mp4",
    "output_video": "http://127.0.0.1:8001/outputs/uuid_tracked.mp4",
    "tracking_csv": "http://127.0.0.1:8001/outputs/uuid_tracking.csv",
    "analytics_json": "http://127.0.0.1:8001/analytics/uuid_analytics.json",
    "heatmaps_dir": "http://127.0.0.1:8001/heatmaps/tracking_uuid/"
  },
  "analytics": { ... }
}
```

---

## 9. Authentication & Security

### 9.1 Authentication Flow

**JWT-Based Authentication**:

```
1. User Registration/Login
   ↓
2. Backend validates credentials
   ↓
3. Backend generates JWT token
   {
     "sub": "user_id",
     "exp": timestamp + 60min
   }
   ↓
4. Frontend stores token in localStorage
   ↓
5. Frontend includes token in all API requests
   Authorization: Bearer <token>
   ↓
6. Backend validates token on each request
   ↓
7. If expired/invalid → 401 Unauthorized
```

### 9.2 Password Security


**Hashing Algorithm**: bcrypt with PassLib
- **Rounds**: 12 (default)
- **Salt**: Automatically generated per password
- **Verification**: Constant-time comparison

```python
# ⚠️ EXAMPLE CODE ONLY - NOT PRODUCTION CODE
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Registration - hash user's password before storing
hashed = pwd_context.hash(plain_password)  # Variable from user input

# Login - verify against stored hash
is_valid = pwd_context.verify(plain_password, hashed_password)  # Variables, not hardcoded
```

**Security Best Practices**:
- Never store plain-text passwords
- Always use bcrypt or Argon2 for password hashing
-  Use minimum 12 rounds (current default)
-  Implement rate limiting on login attempts
-  Enforce strong password policies (8+ chars, mixed case, numbers)

### 9.3 OAuth Integration

**Supported Providers**:
- Google OAuth 2.0
- Apple Sign In

**OAuth Flow**:
```
1. User clicks "Continue with Google"
   ↓
2. Redirect to Google OAuth consent screen
   ↓
3. User authorizes application
   ↓
4. Google redirects back with auth code
   ↓
5. Backend exchanges code for access token
   ↓
6. Backend fetches user profile
   ↓
7. Backend creates/updates user account
   ↓
8. Backend generates JWT token
   ↓
9. Frontend receives token and redirects to dashboard
```

**Environment Variables**:
```bash
#  PLACEHOLDER VALUES - REPLACE WITH ACTUAL CREDENTIALS
# DO NOT COMMIT THESE TO VERSION CONTROL
GOOGLE_CLIENT_ID=your-client-id                    # Replace with actual Google Client ID
GOOGLE_CLIENT_SECRET=your-client-secret            # Replace with actual secret from Google Console
APPLE_CLIENT_ID=your-services-id                   # Replace with actual Apple Services ID
APPLE_TEAM_ID=your-team-id                         # Replace with actual Apple Team ID
APPLE_KEY_ID=your-key-id                           # Replace with actual Apple Key ID
APPLE_PRIVATE_KEY=your-private-key                 # Replace with actual private key content
```

** SECURITY CRITICAL**:
- Never commit OAuth secrets to Git repositories
- Use environment variables or secret managers (AWS Secrets Manager, Azure Key Vault)
-  Rotate credentials regularly (every 90 days recommended)
-  Use different credentials for dev/staging/production environments

### 9.4 Authorization

**Role-Based Access Control**:
- Users can only access their own uploads
- User ID validation on every protected endpoint
- Database foreign key constraints enforce ownership

**Authorization Check**:
```python
# ⚠️ SIMPLIFIED EXAMPLE - Production code includes error handling
def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    # token parameter comes from Authorization header, not hardcoded
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # SECRET_KEY from environment
    user_id = payload.get("sub")
    return int(user_id)

# In endpoint - demonstrates authorization pattern
@router.post("/inference/player/track")
async def run_player_track(req: Request, user_id: int = Depends(get_current_user)):
    rec = get_upload(req.id)
    # Verify user owns the resource
    if rec["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
```

**Authorization Best Practices**:
-  Validate user ownership on every protected endpoint
-  Use dependency injection (Depends) for clean code
-  Return 403 Forbidden (not 404) to prevent information leakage
-  Log authorization failures for security monitoring

### 9.5 Security Best Practices

- **HTTPS**: Should be enabled in production
- **CORS**: Configured to allow specific origins
- **SQL Injection**: Protected by SQLAlchemy ORM
- **XSS**: React escapes by default
- **CSRF**: Not applicable (JWT tokens, no cookies)
- **Rate Limiting**: Should be implemented in production
- **File Upload Validation**: Type and size checks
- **Environment Variables**: Secrets not committed to repository

---

## 10. Core Features

### 10.1 Player Tracking

**Capabilities**:
- Real-time multi-player detection and tracking
- Unique ID assignment across video duration
- Bounding box visualization on output video
- Movement path extraction
- Speed and distance calculations
- Confidence-based filtering

**Output Artifacts**:
1. **Annotated Video**: Bounding boxes + IDs overlaid
2. **Tracking CSV**: Frame-by-frame coordinates
3. **Analytics JSON**: Comprehensive statistics
4. **Individual Heatmaps**: Per-player movement density
5. **Team Heatmap**: Overall team activity
6. **Zone Heatmaps**: Back 50, Midfield, Forward 50

**Metrics Provided**:
- Distance traveled (meters)
- Average speed (m/s and km/h)
- Maximum speed (m/s and km/h)
- Participation time
- Zone-specific activity

### 10.2 Crowd Monitoring

**Capabilities**:
- Automated people detection in crowd scenes
- Frame sampling (every 30th frame for performance)
- Crowd density heatmap generation
- People count per frame
- Temporal density analysis

**Output Artifacts**:
1. **Original Frames**: Sampled frames with detections
2. **Heatmap Images**: Density visualization per frame
3. **Count Metadata**: Number of people detected

**Use Cases**:
- Stadium crowd safety monitoring
- Entry/exit congestion detection
- Emergency evacuation planning
- Capacity management

### 10.3 Heatmap Visualization

**Types of Heatmaps**:

**1. Player Individual Heatmap**
- Shows single player's movement patterns
- High-intensity areas = frequent occupation
- Scaled to AFL oval dimensions

**2. Team Heatmap**
- Aggregated movement of all tracked players
- Identifies hot zones and dead zones
- Strategic positioning analysis

**3. Zone Heatmaps**
- **Back 50**: Defensive positioning
- **Midfield**: Ball contest areas
- **Forward 50**: Offensive pressure

**4. Crowd Density Heatmap**
- Person detection intensity
- Real-time crowd flow visualization

**Visualization Features**:
- AFL oval-shaped mask
- Gaussian smoothing for aesthetic appeal
- Confidence-weighted intensity
- Color gradient (Viridis colormap)
- Scalable resolution (default 200×150 cells)

### 10.4 Video Analysis Pipeline

**End-to-End Workflow**:

```
1. Video Upload
   ↓ (Multipart HTTP)
2. File Storage (PostgreSQL + Disk)
   ↓
3. Inference Request (Player/Crowd)
   ↓
4. Job Status: "Analyzing..."
   ↓
5a. Player Tracking              5b. Crowd Monitoring
    - YOLOv11 Detection              - Frame Sampling
    - ByteTrack Tracking             - External API Call
    - CSV Export                     - Heatmap Download
    - Heatmap Generation
   ↓                             ↓
6. Analytics Storage (PostgreSQL)
   ↓
7. Job Status: "Completed"
   ↓
8. Frontend Display (Dashboard)
```

### 10.5 Reporting & Export

**Report Generation**:
- PDF reports with embedded charts
- CSV data export
- JSON analytics download
- Image gallery (heatmaps)

**Report Contents**:
- Match summary
- Player statistics table
- Heatmap visualizations
- Speed/distance charts
- Zone activity breakdown
- Crowd density timeline (if applicable)

---

## 11. Data Flow & Processing

### 11.1 Video Upload Flow

```
┌─────────────┐
│  Frontend   │
│  (React)    │
└──────┬──────┘
       │ POST /api/v1/uploads/video
       │ multipart/form-data
       ▼
┌─────────────┐
│   Backend   │
│  (FastAPI)  │
├─────────────┤
│ 1. Validate │
│ 2. Save File│
│ 3. Gen UUID │
│ 4. Insert DB│
└──────┬──────┘
       │ Return upload_id
       ▼
┌─────────────┐
│ PostgreSQL  │
│  uploads    │
└─────────────┘
```

### 11.2 Player Tracking Flow

```
Frontend → Backend API → Tracking Service → Backend API → Frontend
   │           │               │                 │           │
   │  Request  │               │                 │           │
   │ ──────────►               │                 │           │
   │           │  Forward File │                 │           │
   │           │ ──────────────►                 │           │
   │           │               │ YOLO Inference  │           │
   │           │               │ ByteTrack       │           │
   │           │               │ Heatmap Gen     │           │
   │           │    ◄──────────┤                 │           │
   │           │  JSON + URLs  │                 │           │
   │           │               │                 │           │
   │           │ Download Files│                 │           │
   │           │ Save to DB    │                 │           │
   │           │ ──────────────────────────────► │           │
   │           │                                 │  Response │
   │ ◄─────────────────────────────────────────────────────┤
   │           Display Results                              │
```

### 11.3 Crowd Monitoring Flow

```
Frontend → Backend API → External Crowd API
   │           │               │
   │  Request  │               │
   │ ──────────►               │
   │           │ Extract Frames│
   │           │ (every 30th)  │
   │           │               │
   │           │  POST frame   │
   │           │ ──────────────►
   │           │               │ Detection
   │           │               │ Heatmap Gen
   │           │  ◄────────────┤
   │           │  PNG + Count  │
   │           │               │
   │           │ Save to Disk  │
   │           │ Insert DB     │
   │           │               │
   │  ◄────────┤               │
   │  Response │               │
```

### 11.4 Analytics Retrieval Flow

```
Frontend Request
   ↓
Backend API
   ↓
Query PostgreSQL
   ├── player_analysis table → Player metrics
   ├── crowd_analysis table → Crowd data
   └── inferences table → Job status
   ↓
Aggregate Results
   ↓
Return JSON
   ↓
Frontend Visualization
   ├── Charts (Recharts)
   ├── Heatmap Display
   └── Statistics Cards
```

---

## 12. Deployment Architecture

### 12.1 Development Environment

**Local Setup**:
```
┌──────────────────────┐
│  Developer Machine   │
├──────────────────────┤
│ Port 8080: Frontend  │← Vite Dev Server
│ Port 8000: Backend   │← Uvicorn (main service)
│ Port 8001: Tracking  │← Uvicorn (tracking service)
│ Port 5432: PostgreSQL│← Docker container
└──────────────────────┘
```

**Commands**:
```bash
# PostgreSQL
docker run --name afl-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=aflvision \
  -p 5432:5432 -d postgres:15

# Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Tracking Service
cd tracking_code
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Install PyTorch with CUDA
pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 \
  --index-url https://download.pytorch.org/whl/cu121
uvicorn main:app --reload --port 8001

# Frontend
cd frontend
pnpm install
pnpm dev  # Runs on port 8080
```


**Components**:
- **CDN**: Cloudflare/AWS CloudFront for static assets
- **Load Balancer**: NGINX or AWS ALB
- **Frontend Containers**: Docker with NGINX serving built SPA
- **Backend Containers**: Docker with Uvicorn + Gunicorn workers
- **Tracking Service**: GPU-enabled instance (AWS P3/P4, GCP A100)
- **Database**: Managed PostgreSQL (AWS RDS, GCP Cloud SQL)
- **Object Storage**: S3/GCS for videos and heatmaps
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

### 12.2 Docker Configuration

**Backend Dockerfile**:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Tracking Service Dockerfile**:
```dockerfile
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y python3.10 python3-pip
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
```

**Docker Compose** (Development):
```yaml
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: aflvision
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+psycopg2://postgres:postgres@postgres:5432/aflvision
      JWT_SECRET: your-secret-key
    depends_on:
      - postgres

  tracking:
    build: ./tracking_code
    ports:
      - "8001:8001"
    runtime: nvidia
    environment:
      NVIDIA_VISIBLE_DEVICES: all

  frontend:
    build: ./frontend
    ports:
      - "8080:8080"
    depends_on:
      - backend

volumes:
  pgdata:
```

### 12.3 CI/CD Pipeline (Proposed)

```
Git Push → GitHub Actions → Build → Test → Deploy
   │           │            │       │       │
   │           │            │       │       ├── Staging
   │           │            │       │       └── Production
   │           │            │       │
   │           │            │       ├── Unit Tests
   │           │            │       ├── Integration Tests
   │           │            │       └── E2E Tests
   │           │            │
   │           │            ├── Docker Images
   │           │            └── Push to Registry
   │           │
   │           ├── Lint (ESLint, Black)
   │           ├── Type Check (TypeScript, mypy)
   │           └── Security Scan
   │
   └── Trigger Workflow
```

---

## 13. Setup & Installation

### 13.1 Prerequisites

**Software Requirements**:
- **Node.js**: v18+ (for frontend)
- **Python**: 3.10 (exact version for compatibility)
- **PostgreSQL**: 15+
- **Docker**: 20+ (optional, for PostgreSQL)
- **NVIDIA GPU**: With CUDA 12.1 (for tracking service)
- **Git**: For version control

**Hardware Requirements**:
- **CPU**: Multi-core processor (4+ cores recommended)
- **RAM**: 16GB minimum, 32GB recommended
- **GPU**: NVIDIA GPU with 8GB+ VRAM (for tracking)
- **Storage**: 50GB+ available space
- **Network**: Stable internet connection

### 13.2 Step-by-Step Installation

#### Step 1: Clone Repository
```bash
git clone https://github.com/your-org/afl-player-tracking.git
cd afl-player-tracking/Player_Tracking/afl_player_tracking_and_crowd_monitoring
```

#### Step 2: Database Setup
```bash
# ⚠️ DEVELOPMENT ONLY - Use strong passwords in production!
# Option A: Docker (Recommended for Development)
docker run --name afl-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \        # ⚠️ CHANGE IN PRODUCTION!
  -e POSTGRES_DB=aflvision \
  -p 5432:5432 \
  -d postgres:15

# Option B: Local PostgreSQL Installation
# Install PostgreSQL 15 and create database
createdb aflvision
```

** PRODUCTION SECURITY**:
-  Never use default passwords like 'postgres' in production
-  Generate strong passwords: `openssl rand -base64 32`
-  Use secret management tools (Docker secrets, Kubernetes secrets)
-  Restrict PostgreSQL network access (localhost only or VPC)
-  Enable SSL/TLS for database connections

#### Step 3: Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create .env file
# ⚠️ IMPORTANT: Replace placeholder values with actual secure credentials!
echo DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/aflvision > .env
echo JWT_SECRET=your-super-secret-key-change-in-production >> .env  # ⚠️ GENERATE SECURE KEY!

# 🔒 GENERATE SECURE JWT SECRET:
# python -c "import secrets; print(secrets.token_urlsafe(32))"

# Run backend
uvicorn main:app --reload --port 8000
```

**SECURITY CHECKLIST**:
- [ ] Replace JWT_SECRET with cryptographically secure random string (32+ bytes)
- [ ] Update database password if not using default
- [ ] Ensure .env is in .gitignore (never commit secrets!)
- [ ] Use different secrets for dev/staging/production

**Verify Backend**:
- Open http://127.0.0.1:8000 → Should see welcome message
- Open http://127.0.0.1:8000/docs → Swagger UI

#### Step 4: Tracking Service Setup
```bash
cd ../tracking_code

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install PyTorch with CUDA 12.1
pip uninstall torch torchvision torchaudio -y
pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 \
  --index-url https://download.pytorch.org/whl/cu121

# Verify CUDA
python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.version.cuda)"
# Expected output: 2.5.1+cu121 True 12.1

# Run tracking service
uvicorn main:app --reload --port 8001
```

**Verify Tracking Service**:
- Open http://127.0.0.1:8001 → Should see tracking service message
- Open http://127.0.0.1:8001/docs → Swagger UI

#### Step 5: Frontend Setup
```bash
cd ../frontend

# Install pnpm (if not installed)
npm install -g pnpm

# Install dependencies
pnpm install

# Run development server
pnpm dev
```

**Verify Frontend**:
- Open http://localhost:8080 → Should see login page

#### Step 6: Crowd Monitoring API (Optional)

**Note**: The crowd monitoring API is an external service. Update the URL in `backend/routes/crowd.py`:

```python
CROWD_API_URL = "https://your-ngrok-url.ngrok-free.app"
```

Contact the crowd monitoring team for the current API endpoint.

### 13.3 Environment Variables Reference

** CRITICAL SECURITY NOTE**: 
- All values below are **PLACEHOLDERS** - replace with actual credentials
- **NEVER** commit .env files to version control
- Use `.gitignore` to exclude .env files
- Rotate secrets regularly (every 90 days)

**Backend (.env)**:
```bash
# Database -  Use strong password in production!
DATABASE_URL=postgresql+psycopg2://postgres:STRONG_PASSWORD_HERE@localhost:5432/aflvision

# Authentication -  MUST be changed! Generate with: python -c "import secrets; print(secrets.token_urlsafe(32))"
JWT_SECRET=REPLACE_WITH_CRYPTOGRAPHICALLY_SECURE_RANDOM_STRING_32_BYTES_MINIMUM

# OAuth (Optional) -  Obtain from Google Cloud Console and Apple Developer Portal
GOOGLE_CLIENT_ID=your-actual-google-client-id-from-console
GOOGLE_CLIENT_SECRET=your-actual-google-client-secret-from-console
APPLE_CLIENT_ID=your-actual-apple-services-id
APPLE_TEAM_ID=your-actual-apple-team-id
APPLE_KEY_ID=your-actual-apple-key-id
APPLE_PRIVATE_KEY=your-actual-apple-private-key-content

# Services (Development URLs shown)
PLAYER_SVC_URL=http://127.0.0.1:8001
```

**How to Generate Secure Secrets**:
```bash
# JWT Secret (Python)
python -c "import secrets; print(secrets.token_urlsafe(32))"

# JWT Secret (OpenSSL)
openssl rand -base64 32

# Database Password
openssl rand -base64 24
```

**Tracking Service**:
```bash
MODEL_PATH=/path/to/best.pt  # Optional, defaults to ./best.pt
```

**Frontend** (optional .env):
```bash
VITE_API_URL=http://127.0.0.1:8000
```

### 13.4 Testing the Installation

** TESTING ONLY**: The credentials below are for local testing. Never use these in production!

```bash
# 1. Test backend health
curl http://127.0.0.1:8000/

# 2. Register a test user ( Use test credentials only!)
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'
  #  Example credentials - replace with your test account

# 3. Login with test credentials
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=testpass123"
  #  Example credentials - replace with your test account

# 4. Upload a video (replace YOUR_TOKEN with actual JWT from step 3)
curl -X POST http://127.0.0.1:8000/api/v1/uploads/video \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@path/to/video.mp4"

# 5. Test tracking service
curl http://127.0.0.1:8001/
```

**Testing Best Practices**:
-  Use separate test accounts (don't test with production credentials)
- Create a test database for development
-  Clear test data regularly
-  Never test payment or sensitive operations with real data

---

## 14. Performance & Optimization

### 14.1 Frontend Performance

**Optimization Strategies**:

1. **Code Splitting**
   - React.lazy() for route-based splitting
   - Dynamic imports for heavy components
   - Reduces initial bundle size

2. **Caching Strategy**
   - TanStack Query caching (5min stale time)
   - Browser localStorage for auth tokens
   - Service Worker for offline support (future)

3. **Bundle Optimization**
   - Vite tree-shaking
   - Minification in production
   - Gzip/Brotli compression

4. **Image Optimization**
   - Lazy loading for heatmaps
   - Responsive images
   - WebP format support

5. **React Performance**
   - React.memo for expensive components
   - useMemo/useCallback for computations
   - Virtual scrolling for long lists (future)

**Metrics**:
- Initial Load: <3s on 4G
- Time to Interactive: <5s
- Lighthouse Score: 90+ (target)

### 14.2 Backend Performance

**Optimization Strategies**:

1. **Async Operations**
   - FastAPI async endpoints
   - Non-blocking I/O
   - Parallel file downloads

2. **Database Optimization**
   - Indexes on foreign keys
   - Connection pooling (SQLAlchemy)
   - Query optimization

3. **Caching**
   - Redis caching layer (future)
   - Static file CDN
   - API response caching

4. **Concurrency**
   - Uvicorn workers
   - Gunicorn process management
   - Background task queues (Celery - future)

**Metrics**:
- API Response Time: <200ms (average)
- Upload Handling: Up to 100MB files
- Concurrent Users: 100+ (with scaling)

### 14.3 Tracking Service Performance

**Optimization Strategies**:

1. **GPU Acceleration**
   - CUDA-enabled PyTorch
   - Batch processing
   - Model quantization (future)

2. **Video Processing**
   - Frame skipping (configurable)
   - Resolution downscaling
   - Hardware-accelerated decoding

3. **Memory Management**
   - Streaming video processing
   - Garbage collection tuning
   - Memory-mapped files

**Metrics**:
- Processing Speed: 60-120 FPS (with GPU)
- Model Inference: ~10ms per frame
- Memory Usage: <8GB VRAM

### 14.4 Database Performance

**Optimization**:
```sql
-- Indexes for fast lookups
CREATE INDEX idx_uploads_user_id ON uploads(user_id);
CREATE INDEX idx_inferences_upload_id ON inferences(upload_id);
CREATE INDEX idx_player_analysis_upload_id ON player_analysis(upload_id);
CREATE INDEX idx_crowd_analysis_upload_id ON crowd_analysis(upload_id);

-- Vacuum and analyze
VACUUM ANALYZE;

-- Connection pooling
pool_size = 20
max_overflow = 10
pool_pre_ping = True
```

### 14.5 Scalability Considerations

**Horizontal Scaling**:
- Stateless backend services
- Load balancer distribution
- Database read replicas
- Object storage for files

**Vertical Scaling**:
- Multi-GPU tracking service
- Increased database resources
- SSD storage for faster I/O

**Future Enhancements**:
- Kubernetes orchestration
- Auto-scaling policies
- Message queue (RabbitMQ/Kafka)
- Microservices decomposition

---

## 15. Testing & Quality Assurance

### 15.1 Testing Strategy

**Test Pyramid**:
```
          ┌─────────────┐
          │  E2E Tests  │  ← Few, slow, comprehensive
          ├─────────────┤
          │Integration  │  ← Medium, API/DB tests
          │    Tests    │
          ├─────────────┤
          │   Unit      │  ← Many, fast, isolated
          │   Tests     │
          └─────────────┘
```

### 15.2 Frontend Testing

**Tools**:
- Vitest: Unit testing
- React Testing Library: Component testing
- Playwright: E2E testing (future)

**Test Cases**:
```typescript
// Example: useDashboardState hook test
import { describe, it, expect } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useDashboardState } from '@/hooks/useDashboardState';

describe('useDashboardState', () => {
  it('should initialize with default values', () => {
    const { result } = renderHook(() => useDashboardState());
    expect(result.current.isVideoUploading).toBe(false);
    expect(result.current.completedAnalyses).toEqual([]);
  });

  it('should update video upload progress', () => {
    const { result } = renderHook(() => useDashboardState());
    act(() => {
      result.current.setVideoUploadProgress(50);
    });
    expect(result.current.videoUploadProgress).toBe(50);
  });
});
```

**Run Tests**:
```bash
cd frontend
pnpm test
pnpm typecheck
```

### 15.3 Backend Testing

**Tools**:
- pytest: Unit and integration testing
- httpx: Async HTTP client testing
- pytest-cov: Code coverage

**Test Cases**:
```python
# ⚠️ TEST CODE EXAMPLE - Uses mock/test data only
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    # ⚠️ Test credentials - not real accounts
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "testpass123"}  # Test data
    )
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_credentials():
    # Testing failure case with intentionally wrong credentials
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "wrong@example.com", "password": "wrongpass"}  # Invalid test data
    )
    assert response.status_code == 401
```

**Testing Security Best Practices**:
- ✅ Use test database (not production database)
- ✅ Mock external API calls (don't hit real services)
- ✅ Clean up test data after tests complete
- ✅ Use fixtures for consistent test data
- ✅ Never commit test credentials to repositories

**Run Tests**:
```bash
cd backend
pytest
pytest --cov=. --cov-report=html
```

### 15.4 Integration Testing

**Test Scenarios**:
1. Complete video upload → tracking → retrieval flow
2. User registration → login → authorized request
3. Crowd monitoring end-to-end
4. Database integrity constraints

### 15.5 Quality Metrics

**Code Quality**:
- **Test Coverage**: Target 80%+
- **Type Safety**: 100% TypeScript, strict mode
- **Linting**: ESLint (frontend), Black (backend)
- **Code Reviews**: Required for all PRs

**Performance Metrics**:
- API latency: <200ms (p95)
- Error rate: <1%
- Uptime: 99.9% (target)

---

## 16. Future Enhancements

### 16.1 Short-Term Roadmap (3-6 months)

1. **Advanced Analytics**
   - Acceleration/deceleration tracking
   - Direction change frequency
   - Player collision detection
   - Formation analysis

2. **Real-Time Processing**
   - WebSocket support for live updates
   - Streaming video analysis
   - Live dashboard updates

3. **Enhanced UI/UX**
   - 3D field visualization
   - Interactive heatmap overlays
   - Video playback with annotations
   - Mobile-responsive design improvements

4. **Performance Optimization**
   - Redis caching layer
   - CDN integration for static files
   - Database query optimization
   - API response compression

5. **Testing & CI/CD**
   - Comprehensive test suites
   - Automated deployment pipeline
   - Staging environment
   - Performance benchmarking

### 16.2 Medium-Term Roadmap (6-12 months)

1. **Machine Learning Enhancements**
   - Player jersey number recognition (OCR)
   - Team color detection and classification
   - Action recognition (kick, mark, tackle)
   - Event detection (goal, behind, free kick)

2. **Multi-Camera Support**
   - Multiple video angle processing
   - 3D position estimation
   - Camera calibration
   - Synchronized analysis

3. **Advanced Crowd Analytics**
   - Emotion detection
   - Crowd flow prediction
   - Anomaly detection (fights, rushes)
   - Real-time alert system

4. **Collaboration Features**
   - Multi-user access with roles
   - Shared analysis sessions
   - Comments and annotations
   - Export to coaching software

5. **Integration Ecosystem**
   - AFL official statistics API
   - Sports analytics platforms
   - Video management systems
   - Third-party data sources

### 16.3 Long-Term Vision (12+ months)

1. **AI-Powered Insights**
   - Predictive analytics (player fatigue, injury risk)
   - Strategic recommendations
   - Opposition analysis
   - Automated highlight generation

2. **Edge Computing**
   - On-device processing for live matches
   - Reduced latency
   - Offline capability
   - Privacy-preserving analysis

3. **Extended Sports Support**
   - Rugby, soccer, basketball adaptation
   - Generic sports tracking framework
   - Custom sport configuration

4. **Commercial Features**
   - Subscription tiers
   - Team management dashboard
   - Broadcasting integration
   - Fan engagement tools

5. **Research Collaboration**
   - Academic partnerships
   - Open dataset publication
   - Research paper contributions
   - Industry conferences

### 16.4 Technical Debt & Improvements

1. **Code Refactoring**
   - Microservices decomposition
   - Improved error handling
   - Consistent naming conventions
   - Documentation updates

2. **Security Enhancements**
   - Penetration testing
   - OAuth scope refinement
   - Rate limiting
   - Input sanitization audit

3. **Infrastructure**
   - Kubernetes deployment
   - Auto-scaling
   - Multi-region support
   - Disaster recovery plan

4. **Monitoring & Observability**
   - Prometheus metrics
   - Grafana dashboards
   - Distributed tracing
   - Log aggregation

---

## Appendix A: Security Guidelines & OWASP Compliance

### A.1 OWASP Top 10 Mitigation Strategies

This section addresses how the system mitigates OWASP Top 10 security risks:

#### A01: Broken Access Control
**Mitigation**:
-  JWT token validation on every protected endpoint
-  User ownership verification (user can only access own uploads)
-  Foreign key constraints enforce data ownership
-  HTTP 403 responses prevent information leakage
- Dependency injection pattern for clean authorization

#### A02: Cryptographic Failures
**Mitigation**:
-  bcrypt password hashing (12 rounds minimum)
-  JWT tokens with HS256 algorithm
-  Automatic salt generation per password
-  No plain-text password storage
- HTTPS required in production
-  Environment variables for secrets (never hardcoded)

#### A03: Injection
**Mitigation**:
-  SQLAlchemy ORM prevents SQL injection
-  Parameterized queries (never string concatenation)
-  Pydantic validation on all API inputs
-  Type checking with TypeScript (frontend)
-  FastAPI automatic input validation

#### A04: Insecure Design
**Mitigation**:
-  Authentication required for all sensitive operations
- Separation of concerns (microservices)
-  Rate limiting recommended for production
-  Cascade delete rules prevent orphaned data
- Comprehensive error handling

#### A05: Security Misconfiguration
**Production Requirements**:
-  Change all default passwords
- Generate secure JWT_SECRET (32+ bytes)
-  Enable HTTPS/TLS
-  Configure CORS with specific origins
-  Disable debug mode in production
-  Set secure cookie flags
-  Regular dependency updates

#### A06: Vulnerable and Outdated Components
**Mitigation Strategy**:
-  Pinned dependency versions (requirements.txt, package.json)
-  Regular security audits (`npm audit`, `pip-audit`)
-  Automated dependency updates (Dependabot recommended)
- LTS versions of core technologies

#### A07: Identification and Authentication Failures
**Mitigation**:
- JWT tokens with 60-minute expiration
- bcrypt password hashing
-  OAuth integration (Google, Apple)
-  Email uniqueness constraint
-  Implement MFA for production (recommended)
-  Account lockout after failed attempts (recommended)

#### A08: Software and Data Integrity Failures
**Mitigation**:
-  JWT signature verification
- Foreign key constraints
- Transaction support (ACID)
-  Input validation with Pydantic
-  Implement checksums for uploaded files (recommended)

#### A09: Security Logging and Monitoring Failures
**Recommendations**:
-  Implement centralized logging (ELK stack)
-  Log authentication failures
-  Monitor authorization denials
-  Alert on suspicious patterns
- Regular security audit reviews

#### A10: Server-Side Request Forgery (SSRF)
**Mitigation**:
- Whitelist for external API URLs
-  No user-controlled URLs in requests
-  Network isolation for microservices
-  Implement URL validation (recommended)

### A.2 Secret Management Best Practices

#### Development Environment
```bash
# Use .env files (NEVER commit to Git)
# .env
DATABASE_URL=postgresql://user:SECURE_PASSWORD@localhost:5432/db
JWT_SECRET=CRYPTOGRAPHICALLY_RANDOM_STRING_32_BYTES_MINIMUM
```

#### Production Environment
**DO NOT use .env files in production!**

**Option 1: AWS Secrets Manager**
```python
import boto3
import json

def get_secret(secret_name):
    client = boto3.client('secretsmanager', region_name='us-east-1')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

# Usage
secrets = get_secret('afl-vision/production')
JWT_SECRET = secrets['JWT_SECRET']
```

**Option 2: Azure Key Vault**
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://afl-vision.vault.azure.net", credential=credential)
JWT_SECRET = client.get_secret("JWT-SECRET").value
```

**Option 3: Kubernetes Secrets**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: afl-vision-secrets
type: Opaque
stringData:
  JWT_SECRET: <base64-encoded-secret>
  DATABASE_PASSWORD: <base64-encoded-password>
```

### A.3 Password Security Policy

**Minimum Requirements** (Recommended for Production):
- Minimum length: 12 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character
- Not in common password dictionary
- Not similar to username/email

**Implementation Example**:
```python
import re
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def validate_password_strength(password: str) -> tuple[bool, str]:
    """Validate password meets security requirements."""
    if len(password) < 12:
        return False, "Password must be at least 12 characters"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain special character"
    return True, "Password is strong"
```

### A.4 API Security Checklist

**Before Production Deployment**:
- [ ] All API endpoints require authentication (except /register, /login)
- [ ] Rate limiting configured (recommended: 100 requests/minute per IP)
- [ ] CORS restricted to specific origins
- [ ] Input validation on all endpoints (Pydantic models)
- [ ] Output sanitization prevents XSS
- [ ] File upload size limits enforced (max 100MB)
- [ ] File type validation (only mp4, avi, mov allowed)
- [ ] SQL injection prevented (ORM only)
- [ ] HTTPS/TLS enabled
- [ ] Security headers configured:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `X-XSS-Protection: 1; mode=block`
  - `Strict-Transport-Security: max-age=31536000`
  - `Content-Security-Policy` defined

### A.5 Penetration Testing Recommendations

**Before Production Launch**:
1. **Automated Scanning**:
   - OWASP ZAP scan
   - Burp Suite Professional
   - Nessus vulnerability scan

2. **Manual Testing**:
   - Authentication bypass attempts
   - Authorization escalation attempts
   - SQL injection testing
   - XSS testing
   - CSRF testing
   - File upload attacks
   - API fuzzing

3. **Third-Party Audit**:
   - Professional penetration testing firm
   - OWASP ASVS Level 2 compliance
   - Annual security audits

### A.6 Incident Response Plan

**Security Incident Detected**:
1. **Immediate Actions**:
   - Isolate affected systems
   - Preserve logs and evidence
   - Notify security team
   - Document timeline

2. **Investigation**:
   - Identify attack vector
   - Assess data exposure
   - Determine scope of compromise

3. **Remediation**:
   - Patch vulnerabilities
   - Rotate all secrets
   - Reset compromised passwords
   - Update security controls

4. **Communication**:
   - Notify affected users
   - Report to regulatory bodies (if required)
   - Document lessons learned

### A.7 Security Contact Information

**Reporting Security Issues**:
- Email: security@your-organization.com
- Encrypted: PGP Key ID: [Your Key ID]
- Bug Bounty: [Program URL if applicable]

**Response Time**:
- Critical: 4 hours
- High: 24 hours
- Medium: 72 hours
- Low: 1 week

---

## Appendix B: Glossary

**AFL**: Australian Football League

**API**: Application Programming Interface

**ByteTrack**: Multi-object tracking algorithm

**CORS**: Cross-Origin Resource Sharing

**CRUD**: Create, Read, Update, Delete

**CSV**: Comma-Separated Values

**CUDA**: Compute Unified Device Architecture (NVIDIA GPU platform)

**DeepSORT**: Deep Simple Online and Realtime Tracking

**FastAPI**: Modern Python web framework

**FPS**: Frames Per Second

**GPU**: Graphics Processing Unit

**Heatmap**: Visual representation of data density

**IOU**: Intersection over Union (overlap metric)

**JWT**: JSON Web Token

**ORM**: Object-Relational Mapping

**PostgreSQL**: Open-source relational database

**REST**: Representational State Transfer

**SPA**: Single Page Application

**SQLAlchemy**: Python SQL toolkit and ORM

**TailwindCSS**: Utility-first CSS framework

**TypeScript**: Typed superset of JavaScript

**Uvicorn**: ASGI server for Python

**Vite**: Frontend build tool

**YOLO**: You Only Look Once (object detection)

---

## Appendix C: Troubleshooting

### Common Issues

**Issue**: Database connection failed
```
Solution:
1. Verify PostgreSQL is running: docker ps
2. Check DATABASE_URL in .env
3. Ensure port 5432 is not in use
4. Test connection: psql -h localhost -U postgres -d aflvision
```

**Issue**: CUDA not available
```
Solution:
1. Verify GPU: nvidia-smi
2. Check CUDA installation: nvcc --version
3. Reinstall PyTorch with CUDA:
   pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 \
     --index-url https://download.pytorch.org/whl/cu121
4. Test: python -c "import torch; print(torch.cuda.is_available())"
```

**Issue**: Frontend 401 Unauthorized
```
Solution:
1. Check if token is stored: localStorage.getItem('authToken')
2. Re-login to refresh token
3. Verify backend is running on port 8000
4. Check browser console for errors
```

**Issue**: Video upload fails
```
Solution:
1. Check file size (must be <100MB typically)
2. Verify file format (MP4 recommended)
3. Check backend logs for errors
4. Ensure uploaded_videos/ directory exists
```

---

## Appendix D: API Quick Reference

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `/api/v1/auth/register` | POST | No | Create account |
| `/api/v1/auth/login` | POST | No | Get JWT token |
| `/api/v1/uploads/video` | POST | Yes | Upload video |
| `/api/v1/uploads/list` | GET | Yes | List uploads |
| `/api/v1/inference/player/track` | POST | Yes | Run tracking |
| `/api/v1/inference/crowd/{id}` | POST | Yes | Run crowd analysis |
| `/api/v1/inference/inferences` | GET | Yes | Get job status |
| `/api/v1/analysis/player/{upload_id}/player/{player_id}` | GET | Yes | Get player data |
| `/api/v1/analysis/crowd/{upload_id}` | GET | Yes | Get crowd data |

---
**End of Technical Documentation**

*For updates and corrections, please submit a pull request to the documentation repository.*


---


