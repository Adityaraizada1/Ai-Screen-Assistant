import React from 'react'

function App() {
  const features = [
    { title: 'Global Hotkey', desc: 'Invoke intelligence instantly with Ctrl + Option + A.', icon: '🎹' },
    { title: 'Instant Vision', desc: 'Captures your screen and analyzes it with Qwen2-VL.', icon: '📸' },
    { title: 'Voice Interaction', desc: 'Natural speech-to-text powered by OpenAI Whisper.', icon: '🎙️' },
    { title: 'Safety Guard', desc: 'Built-in protection for academic and sensitive contexts.', icon: '🛡️' },
  ];

  const techStack = [
    { name: 'Qwen2-VL', cat: 'Vision' },
    { name: 'Whisper', cat: 'Voice' },
    { name: 'PyTorch', cat: 'Engine' },
    { name: 'CustomTK', cat: 'UI' },
  ];

  return (
    <div className="container min-h-screen">
      {/* Header */}
      <nav style={{ padding: '40px 0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2 style={{ fontSize: '24px', fontWeight: '800' }}>AI<span className="premium-gradient-text">Screen</span></h2>
        <button className="btn-primary" onClick={() => window.open('https://github.com/Adityaraizada1/Ai-Screen-Assistant', '_blank')}>View GitHub</button>
      </nav>

      {/* Hero Section */}
      <section style={{ textAlign: 'center', padding: '100px 0 60px' }} className="animate-fade-in">
        <h1 style={{ fontSize: 'clamp(40px, 8vw, 80px)', fontWeight: '800', lineHeight: '1.1', marginBottom: '24px' }}>
          Vision Meets <span className="premium-gradient-text">Voice</span>
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '20px', maxWidth: '600px', margin: '0 auto 40px', lineHeight: '1.6' }}>
          An advanced AI assistant that sees your desktop and hears your voice. Context-aware intelligence at your fingertips.
        </p>
        <div style={{ display: 'flex', gap: '16px', justifyContent: 'center' }}>
          <button className="btn-primary">Get Started</button>
          <button className="glass" style={{ padding: '12px 24px', borderRadius: '9999px', color: 'white', border: '1px solid var(--glass-border)', cursor: 'pointer' }}>Watch Demo</button>
        </div>
      </section>

      {/* Terminal Mockup */}
      <div className="glass" style={{ maxWidth: '800px', margin: '0 auto 100px', padding: '24px', fontFamily: 'monospace', color: '#10b981' }}>
        <div style={{ borderBottom: '1px solid var(--glass-border)', marginBottom: '16px', paddingBottom: '8px', display: 'flex', gap: '8px' }}>
          <div style={{ width: '12px', height: '12px', borderRadius: '50%', background: '#ef4444' }}></div>
          <div style={{ width: '12px', height: '12px', borderRadius: '50%', background: '#f59e0b' }}></div>
          <div style={{ width: '12px', height: '12px', borderRadius: '50%', background: '#10b981' }}></div>
        </div>
        <div>
          <p>$ python main.py</p>
          <p style={{ color: 'var(--text-primary)' }}>🎹 Press Ctrl + Option + A to analyze...</p>
          <p>📸 Capturing screen...</p>
          <p>🎙 Listening for 5 seconds...</p>
          <p>🧠 AI Thinking...</p>
          <p style={{ color: '#3b82f6' }}>🤖 RESPONSE: This is a complex graph showing market trends...</p>
        </div>
      </div>

      {/* Features Grid */}
      <section style={{ padding: '60px 0' }}>
        <h2 style={{ textAlign: 'center', fontSize: '36px', marginBottom: '48px' }}>Powerful <span className="premium-gradient-text">Capabilities</span></h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '24px' }}>
          {features.map((f, i) => (
            <div key={i} className="glass" style={{ padding: '32px', transition: 'all 0.3s' }}>
              <div style={{ fontSize: '32px', marginBottom: '16px' }}>{f.icon}</div>
              <h3 style={{ marginBottom: '12px', fontSize: '20px' }}>{f.title}</h3>
              <p style={{ color: 'var(--text-secondary)', lineHeight: '1.5' }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Tech Stack */}
      <section style={{ padding: '100px 0 140px', textAlign: 'center' }}>
        <h2 style={{ fontSize: '24px', color: 'var(--text-secondary)', marginBottom: '40px', letterSpacing: '2px', textTransform: 'uppercase' }}>Built With</h2>
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '40px' }}>
          {techStack.map((tech, i) => (
            <div key={i} style={{ textAlign: 'left' }}>
              <div style={{ fontSize: '12px', textTransform: 'uppercase', color: 'var(--accent-blue)', fontWeight: 'bold' }}>{tech.cat}</div>
              <div style={{ fontSize: '24px', fontWeight: '800' }}>{tech.name}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer style={{ padding: '40px 0', textAlign: 'center', borderTop: '1px solid var(--glass-border)', color: 'var(--text-secondary)' }}>
        <p>© 2026 AI Screen Assistant. Made with AI for AI.</p>
      </footer>
    </div>
  )
}

export default App
