# 🏋️ AI Real-time GYM Trainer

An intelligent real-time fitness coaching application that uses advanced computer vision and AI to detect exercise form, provide instant feedback, and guide users through their workout sessions with voice coaching and performance tracking.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**AI Real-time GYM Trainer** is a web-based fitness application that leverages cutting-edge computer vision and artificial intelligence to deliver personalized, real-time coaching. The application monitors user movements, analyzes exercise form, detects form deviations, and provides corrective guidance through AI-powered voice coaching.

### Core Capabilities
- ✅ Real-time pose detection and analysis
- ✅ Exercise form validation with angle-based metrics
- ✅ AI voice coaching using LLMs (Groq API)
- ✅ Multi-exercise support (Squats, Push-ups, Biceps Curls, Shoulder Press, Lunges)
- ✅ Persistent workout history and analytics
- ✅ User authentication system
- ✅ Real-time performance metrics tracking

---

## ✨ Key Features

### 1. **Real-time Pose Detection**
   - MediaPipe-based pose estimation
   - 33-point body landmark detection
   - Sub-millisecond inference latency

### 2. **Exercise-Specific Metrics**
   - **Squats**: Knee angle, back angle, depth status
   - **Push-ups**: Elbow angle, body alignment, hip position
   - **Biceps Curls**: Elbow angle, shoulder stability, swing detection
   - **Shoulder Press**: Elbow angle, arm extension, back arch
   - **Lunges**: Front knee angle, torso angle, balance status

### 3. **AI Voice Coaching**
   - Integration with Groq LLM for intelligent feedback
   - Text-to-speech conversion
   - Event-driven coaching (workout started, rep completed, form correction, workout end)

### 4. **Workout Tracking**
   - SQLite-based persistence
   - Historical workout analytics
   - Session statistics and progress metrics

### 5. **User Authentication**
   - Simple login/registration system
   - Session-based user management
   - User-specific workout history

### 6. **Responsive UI**
   - Real-time metrics display
   - Live video streaming
   - Interactive workout controls
   - Historical data visualization

---

## 🛠 Tech Stack

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Streamlit** | Latest | Web application framework |
| **Streamlit WebRTC** | Latest | Real-time video streaming |
| **CSS Custom** | - | Styling & animations |

### Vision & Processing
| Technology | Version | Purpose |
|-----------|---------|---------|
| **MediaPipe** | 0.10+ | Human pose estimation |
| **OpenCV** | 4.8+ | Video processing & rendering |
| **NumPy** | 1.24+ | Numerical computations |

### AI & Coaching
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Groq SDK** | Latest | LLM inference for coaching |
| **pyttsx3** | 2.90+ | Text-to-speech synthesis |
| **Python Audio** | - | Audio playback & streaming |

### Data & Storage
| Technology | Version | Purpose |
|-----------|---------|---------|
| **SQLite3** | Built-in | Lightweight database |
| **Pandas** | 2.0+ | Data manipulation & analytics |

### Development
| Tool | Version | Purpose |
|-----|---------|---------|
| **Python** | 3.9+ | Runtime environment |
| **Git** | Latest | Version control |

### Tech Stack Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      FRONTEND LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│  • Streamlit          - Web UI framework                        │
│  • Streamlit WebRTC   - Real-time video streaming              │
│  • CSS Custom         - Styling & animations                   │
└─────────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    VISION & TRACKING LAYER                      │
├─────────────────────────────────────────────────────────────────┤
│  • MediaPipe          - Pose detection & landmarks             │
│  • OpenCV             - Video processing & rendering           │
│  • NumPy              - Numerical computations                 │
└─────────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  AI & COACHING LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│  • Groq LLM           - Large Language Model inference          │
│  • pyttsx3            - Text-to-Speech synthesis               │
│  • Python Audio       - Audio playback & streaming             │
└──────────────────────────────────────────────────��──────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PERSISTENCE LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│  • SQLite3            - Lightweight relational database         │
│  • Pandas             - Data manipulation & analytics           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗 Architecture

### System Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                      USER BROWSER                               │
│  ┌──────���─────────────────────────────────────────────────────┐ │
│  │         Streamlit Web Interface (React-based)             │ │
│  │  ┌──────────────┐  ┌──────────┐  ┌──────────────────────┐ │ │
│  │  │   Sidebar    │  │  Main    │  │  Metrics Display     │ │ │
│  │  │  - Workout   │  │  - Video │  │  - Form Feedback     │ │ │
│  │  │    Config    │  │  - Stream│  │  - Real-time Stats   │ │ │
│  │  │  - History   │  │  - Coach │  │  - History Table     │ │ │
│  │  │    Table     │  │  - Chat  │  │                      │ │ │
│  │  └──────────────┘  └──────────┘  └──────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
                              │
                    WebRTC Connection
                    (Secure Streaming)
                              │
         ┌────────────────────┴────────────────────┐
         │                                         │
┌────────▼──────────┐                  ┌──────────▼──────────┐
│   Video Capture   │                  │  Backend (Python)  │
│   - Browser Cam   │                  │                    │
│   - H.264 Codec   │◄─────Frames─────►│ ┌────────────────┐ │
│   - 30 FPS        │                  │ │ SessionState   │ │
└───────────────────┘                  │ │ Management     │ │
                                       │ └────────────────┘ │
                                       │                    │
                                       │ ┌────────────────┐ │
                                       │ │ Video Stream   │ │
                                       │ │ Processor      │ │
                                       │ │ (async)        │ │
                                       │ └────────┬───────┘ │
                                       └──────────┼──────────┘
                                                  │
                        ┌─────────────────────────┼─────────────────────────┐
                        │                         │                         │
          ┌─────────────▼────────────┐  ┌────────▼────────┐  ┌────────────▼─────┐
          │   Vision Processing      │  │  AI Coaching    │  │  Persistence     │
          │                          │  │                 │  │                  │
          │ ┌────────────────────┐   │  │ ┌─────────────┐ │  │ ┌──────────────┐ │
          │ │ MediaPipe Pose     │   │  │ │ Groq LLM    │ │  │ │ SQLite DB    │ │
          │ │ Detection          │   │  │ │ - Analysis  │ │  │ │ - Users      │ │
          │ └─────────┬──────────┘   │  │ │ - Feedback  │ │  │ │ - Exercises  │ │
          │           │              │  │ └─────────────┘ │  │ │ - Sessions   │ │
          │ ┌─────────▼──────────┐   │  │                 │  │ └──────────────┘ │
          │ │ Angle Calculator   │   │  │ ┌─────────────┐ │  │                  │
          │ │ (Knee, Elbow, etc) │   │  │ │ Text-to-    │ │  │ ┌──────────────┐ │
          │ └─────────┬──────────┘   │  │ │ Speech (TTS)│ │  │ │ Data Sync    │ │
          │           │              │  │ │             │ │  │ │ - Metrics    │ │
          │ ┌─────────▼──────────┐   │  │ └─────────────┘ │  │ │ - Feedback   │ │
          │ │ Exercise Metrics   │   │  │                 │  │ └──────────────┘ │
          │ │ Validation         │   │  │ ┌─────────────┐ │  │                  │
          │ └────────────────────┘   │  │ │ Audio Play  │ │  │                  │
          │                          │  │ │ Pipeline    │ │  │                  │
          │                          │  │ └─────────────┘ │  │                  │
          └──────────────────────────┘  └─────────────────┘  └──────────────────┘
```

### Component Description

**Frontend Layer**
- Streamlit-based responsive UI
- Real-time video streaming via WebRTC
- Interactive workout configuration
- Live metrics and feedback display

**Vision Processing Layer**
- MediaPipe for 33-point pose detection
- OpenCV for frame processing and rendering
- Angle calculations for joint measurements
- Exercise-specific form validation

**AI Coaching Layer**
- Groq LLM for intelligent feedback generation
- Text-to-speech for audio coaching
- Event-driven coaching pipeline
- Real-time audio playback

**Persistence Layer**
- SQLite database for user and workout data
- Pandas for data aggregation and analytics
- Session management and history tracking

---

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- Webcam/Camera for video input
- Internet connection (for Groq API)
- Modern web browser with WebRTC support

### Step 1: Clone Repository
```bash
git clone https://github.com/Sushantyadav0I3IT0/AI-REALTIME-GYM-trainer-.git
cd AI-REALTIME-GYM-trainer-
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Environment Variables
```bash
# Create .env file or set environment variables
export GROQ_API_KEY="your_groq_api_key_here"
```

### Step 5: Configure Streamlit
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#0F1419"
secondaryBackgroundColor = "#31333D"
textColor = "#FAFAFA"
font = "sans serif"

[client]
showErrorDetails = true
```

### Step 6: Run Application
```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

---

## 🚀 Usage

### Getting Started

1. **Access the Application**
   - Open browser to `http://localhost:8501`
   - Login with credentials (or create new account)

2. **Configure Your Workout**
   - Select exercise from dropdown (Squats, Push-ups, etc.)
   - Set number of sets (e.g., 3)
   - Set reps per set (e.g., 15)
   - Click "Start Workout"

3. **Perform Exercise**
   - Position yourself in front of webcam
   - Perform exercise with good form
   - AI coach provides real-time feedback
   - Voice coaching guides you through reps

4. **Track Progress**
   - View real-time metrics in sidebar
   - Monitor angle measurements
   - Track completed reps and sets
   - Receive AI coaching feedback

5. **End Workout**
   - Click "End Workout" when finished
   - AI coach provides completion feedback
   - Workout automatically saved to history

6. **View History**
   - Scroll to "Workout History" section
   - View past workouts with metrics
   - Track progress over time

---

## 📁 Project Structure

```
AI-REALTIME-GYM-trainer-/
│
├── main.py                              # Application entry point
│
├── services/                            # Core business logic
│   ├── auth/
│   │   └── login_wall.py               # User authentication
│   │
│   ├── state/
│   │   └── session_defaults.py         # Session state initialization
│   │
│   ├── config/
│   │   └── workout_config.py           # Exercise & workout configs
│   │
│   ├── ui/
│   │   ├── style_loader.py             # CSS/styling management
│   │   └── component_builder.py        # UI component builders
│   │
│   ├── vision/
│   │   ├── exercise_video_processor.py # Video processing pipeline
│   │   ├── pose_detector.py            # MediaPipe integration
│   │   └── angle_calculator.py         # Joint angle calculations
│   │
│   ├── tracking/
│   │   ├── metrics.py                  # Real-time metrics sync
│   │   ├── rep_counter.py              # Rep detection logic
│   │   └── form_validator.py           # Form quality checks
│   │
│   ├── coaching/
│   │   ├── llm.py                      # Groq LLM integration
│   │   ├── tts.py                      # Text-to-speech
│   │   └── voice_pipeline.py           # Voice coaching pipeline
│   │
│   └── persistence/
│       └── exercise_repository.py      # Database operations
│
├── detectors/                           # Specialized exercise detectors
│   ├── squat_detector.py               # Squat-specific logic
│   ├── pushup_detector.py              # Push-up-specific logic
│   ├── curl_detector.py                # Curl-specific logic
│   └── [other_detectors.py]
│
├── ml_models/                           # ML model storage
│   └── [model_files.bin]               # Trained models
│
├── static/                              # Static assets
│   ├── style.css                        # Custom CSS
│   ├── AdobeClean.otf                  # Font files
│   └── [images/icons]
│
├── tutorialinfo/                        # Documentation/guides
│   └── [tutorial_files]
│
├── requirements.txt                     # Python dependencies
├── .gitignore                           # Git ignore rules
├── .env.example                         # Environment template
└── README.md                            # This file
```

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `services/` | Modular business logic (auth, vision, AI, DB) |
| `detectors/` | Exercise-specific detection algorithms |
| `ml_models/` | Pre-trained model weights |
| `static/` | CSS, fonts, and UI assets |
| `tutorialinfo/` | User guides and documentation |

---

## ⚙️ Configuration

### Workout Configuration

Exercises are configured in `services/config/workout_config.py`:

```python
EXERCISE_OPTIONS = [
    "Squats",
    "Push-ups",
    "Biceps Curls (Dumbbell)",
    "Shoulder Press",
    "Lunges"
]
```

### Environment Variables

```bash
# Required
GROQ_API_KEY=xxx_your_groq_api_key_xxx

# Optional
DEBUG=false
LOG_LEVEL=INFO
DATABASE_PATH=./data/exercises.db
```

### Streamlit Secrets (`.streamlit/secrets.toml`)

```toml
GROQ_API_KEY = "your_key_here"
```

---

## 🚀 Future Enhancements

### Phase 2 - Advanced Analytics
- Machine learning model for form prediction
- Injury risk assessment
- Personalized workout recommendations
- Progress trend analysis

### Phase 3 - Social & Gamification
- Leaderboards and challenges
- Achievement badges and milestones
- Social workout sharing
- Friend connections and competitions

### Phase 4 - Extended Exercises
- Deadlifts with form analysis
- Bench press tracking
- Leg press mechanics
- Rows and pull-ups
- Planks and core exercises

### Phase 5 - Mobile & Offline
- React Native mobile app
- Offline mode with local processing
- Cloud sync capabilities
- Native camera optimization

### Phase 6 - Advanced AI
- Fine-tuned LLM models per exercise
- Multimodal learning (video + audio)
- Predictive performance modeling
- Adaptive difficulty adjustment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Code Standards
- Follow PEP 8 style guide
- Add docstrings to all functions
- Include unit tests for new features
- Update README for significant changes

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💻 Author

**Sushant Yadav**
- GitHub: [@Sushantyadav0I3IT0](https://github.com/Sushantyadav0I3IT0)

---

## Acknowledgments

- **MediaPipe** - For robust pose detection
- **Groq** - For high-speed LLM inference
- **Streamlit** - For rapid web development
- **OpenCV** - For computer vision tools
- Fitness community for inspiration and feedback

---

**Last Updated:** October 2026
**Status:** Active Development
**Python Version:** 3.9+
