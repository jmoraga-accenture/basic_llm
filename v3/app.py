# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Hearts of Iron IV Script Generator - v3

A Flask web application that uses OpenAI GPT-4o to generate Hearts of Iron IV 
scripting code from natural language requests with comprehensive HOI4 knowledge 
and guardrails.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI

app = Flask(__name__)

class ConfigManager:
    """Handles configuration loading and validation."""
    
    def __init__(self, config_path: str = "config/config.json"):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            if not os.path.exists(self.config_path):
                raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
            
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            
            # Validate required fields
            if 'openai' not in config:
                raise ValueError("Missing 'openai' configuration section")
            
            openai_config = config['openai']
            required_fields = ['api_key', 'model']
            for field in required_fields:
                if field not in openai_config:
                    raise ValueError(f"Missing required field: openai.{field}")
            
            return config
            
        except Exception as e:
            raise RuntimeError(f"Configuration error: {str(e)}")
    
    def get_openai_config(self) -> Dict[str, Any]:
        """Get OpenAI configuration."""
        return self.config['openai']


class HOI4AIGenerator:
    """OpenAI-powered HOI4 script generator with comprehensive instructions."""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager.get_openai_config()
        self.client = OpenAI(api_key=self.config['api_key'])
        self.system_prompt = self._build_system_prompt()
    
    def _build_system_prompt(self) -> str:
        """Build comprehensive system prompt with HOI4 knowledge and guardrails."""
        return """You are a Hearts of Iron IV (HOI4) scripting expert and code generator. Your task is to generate valid, syntactically correct HOI4 mod code based on user requests.

CRITICAL RULES - ALWAYS FOLLOW:
1. Start with file path comment: # File: path/to/file.txt
2. Generate ONLY valid HOI4 syntax
3. Include explanatory comments throughout
4. Use proper indentation (4 spaces or tabs)
5. Generate localization when appropriate
6. Follow HOI4 modding best practices
7. Use meaningful variable names

HOI4 SYNTAX REFERENCE:

DECISIONS:
# File: common/decisions/category_name.txt
category_name = {
    decision_name = {
        icon = icon_name
        available = {
            # Trigger conditions
        }
        visible = {
            # Visibility conditions  
        }
        cost = number  # Political power cost
        ai_will_do = {
            factor = number
        }
        complete_effect = {
            # Effects when completed
        }
    }
}

EVENTS:
# File: events/event_file.txt
add_namespace = namespace_name

country_event = {
    id = namespace.id
    title = namespace.id.t
    desc = namespace.id.d
    picture = GFX_event_picture
    
    is_triggered_only = yes/no
    trigger = {
        # Trigger conditions
    }
    
    option = {
        name = namespace.id.a
        # Option effects
    }
}

NATIONAL FOCUSES:
# File: common/national_focus/focus_tree.txt
focus_tree = {
    id = tree_id
    country = {
        factor = 0
        modifier = {
            # Country conditions
        }
    }
    
    focus = {
        id = focus_id
        icon = GFX_focus_icon
        cost = number
        prerequisite = { focus = prerequisite_focus }
        available = {
            # Availability conditions
        }
        completion_reward = {
            # Completion effects
        }
    }
}

MODIFIERS:
# File: common/modifiers/modifier_file.txt
modifier_name = {
    # Modifier effects
    modifier_type = value
}

COMMON EFFECTS:
- add_political_power = number
- add_war_support = decimal
- add_stability = decimal
- add_manpower = number
- add_equipment_to_stockpile = { type = equipment_type amount = number }
- every_owned_state = { # state scope effects }
- every_neighbor_country = { # neighbor effects }
- set_country_flag = flag_name
- add_ideas = idea_name
- remove_ideas = idea_name

COMMON TRIGGERS:
- has_political_power > number
- has_war_support > decimal
- has_stability > decimal
- has_manpower > number
- has_equipment = { equipment_type > number }
- is_in_war = yes/no
- has_country_flag = flag_name
- tag = COUNTRY_TAG

LOCALIZATION FORMAT:
# File: localisation/english/file_name_l_english.yml
l_english:
 key_name:0 "Display Text"
 key_name_desc:0 "Description text."

SCOPE USAGE:
- Country scope: Effects that apply to nations
- State scope: Effects that apply to states/provinces  
- Character scope: Effects for leaders/generals
- ROOT = current scope country
- FROM = event sender/target
- PREV = previous scope

EXAMPLE PATTERNS:

PRODUCTIVITY BOOST:
Use decisions with dynamic modifiers affecting states:
every_owned_state = {
    add_dynamic_modifier = {
        modifier = modifier_name
        days = -1  # Permanent
    }
}

POLITICAL POWER EVENTS:
Use country_events with add_political_power effect

TECHNOLOGY FOCUSES:
Use completion_reward with add_tech_bonus or unlock_technology

OUTPUT FORMAT:
1. Start with file path comment
2. Generate complete, valid HOI4 code
3. Add explanatory comments
4. Include localization if needed
5. Use proper formatting and indentation

REMEMBER: Generate working HOI4 code that follows proper syntax and modding conventions."""

    def generate_code(self, user_request: str) -> Dict[str, Any]:
        """Generate HOI4 code using OpenAI API."""
        try:
            if not user_request.strip():
                return {
                    'success': False,
                    'error': 'Request cannot be empty',
                    'suggestion': 'Please provide a description of what you want to achieve in HOI4'
                }
            
            # Prepare the prompt
            user_prompt = f"""Generate Hearts of Iron IV scripting code for the following request:

"{user_request}"

Please provide complete, valid HOI4 code with file paths, proper syntax, explanatory comments, and localization if needed."""

            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.config['model'],
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=self.config.get('max_tokens', 2000),
                temperature=self.config.get('temperature', 0.1),
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            
            generated_code = response.choices[0].message.content.strip()
            
            # Basic validation
            if not generated_code:
                return {
                    'success': False,
                    'error': 'OpenAI returned empty response',
                    'suggestion': 'Please try rephrasing your request'
                }
            
            return {
                'success': True,
                'code': generated_code,
                'model_used': self.config['model'],
                'tokens_used': response.usage.total_tokens if response.usage else 'Unknown'
            }
            
        except openai.AuthenticationError:
            return {
                'success': False,
                'error': 'OpenAI API authentication failed',
                'suggestion': 'Please check your API key in config/config.json'
            }
        
        except openai.RateLimitError:
            return {
                'success': False,
                'error': 'OpenAI API rate limit exceeded',
                'suggestion': 'Please wait a moment and try again'
            }
        
        except openai.APIError as e:
            return {
                'success': False,
                'error': f'OpenAI API error: {str(e)}',
                'suggestion': 'Please check your internet connection and try again'
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}',
                'suggestion': 'Please try again or check the application logs'
            }


# Initialize components
try:
    config_manager = ConfigManager()
    hoi4_generator = HOI4AIGenerator(config_manager)
    print("✅ Configuration loaded successfully")
    print(f"🤖 Using OpenAI model: {config_manager.get_openai_config()['model']}")
except Exception as e:
    print(f"❌ Configuration error: {e}")
    print("📝 Please ensure config/config.json exists with valid OpenAI API key")
    hoi4_generator = None


@app.route('/')
def index():
    """Render the main application page."""
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def generate_code():
    """Generate HOI4 code using OpenAI API."""
    if hoi4_generator is None:
        return jsonify({
            'success': False,
            'error': 'Application not properly configured',
            'suggestion': 'Please check config/config.json file'
        })
    
    try:
        data = request.get_json()
        user_request = data.get('request', '')
        
        if not user_request.strip():
            return jsonify({
                'success': False, 
                'error': 'Request cannot be empty',
                'suggestion': 'Please describe what you want to achieve in HOI4'
            })
        
        # Generate the code using OpenAI
        result = hoi4_generator.generate_code(user_request)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}',
            'suggestion': 'Please try again or contact support'
        })


@app.route('/api/examples')
def get_examples():
    """Get example requests for the interface."""
    examples = [
        {
            'title': 'Land Productivity Boost (Primary Test Case)',
            'request': 'Create code to increment all the user\'s land productivity by 10%',
            'description': 'Generate a decision system to boost state productivity'
        },
        {
            'title': 'Political Power Event',
            'request': 'Create an event that gives the player 100 political power',
            'description': 'Generate a country event that awards political power'
        },
        {
            'title': 'Technology Focus',
            'request': 'Make a national focus that unlocks advanced tank technology',
            'description': 'Generate a focus tree entry for tank research bonuses'
        },
        {
            'title': 'Diplomatic Relations',
            'request': 'Create a decision to improve relations with all neighbors by 25',
            'description': 'Generate a decision for diplomatic outreach'
        },
        {
            'title': 'Industrial National Spirit',
            'request': 'Generate code for a national spirit that increases factory output by 15%',
            'description': 'Generate an idea that boosts industrial capacity'
        },
        {
            'title': 'War Trigger Event',
            'request': 'Create an event that triggers when Germany declares war on Poland',
            'description': 'Generate an event for historical war scenarios'
        },
        {
            'title': 'Military Equipment',
            'request': 'Create a decision to add 1000 infantry equipment to stockpile',
            'description': 'Generate equipment management decision'
        },
        {
            'title': 'Research Bonus',
            'request': 'Make a focus that gives +50% research speed for doctrine technologies',
            'description': 'Generate research speed modifier focus'
        }
    ]
    
    return jsonify({'examples': examples})


@app.route('/api/health')
def health_check():
    """Check application health and configuration status."""
    if hoi4_generator is None:
        return jsonify({
            'status': 'error',
            'message': 'Configuration error - check config/config.json'
        }), 500
    
    return jsonify({
        'status': 'healthy',
        'openai_configured': True,
        'model': config_manager.get_openai_config()['model']
    })


if __name__ == '__main__':
    print("🎮 Hearts of Iron IV Script Generator - v3")
    print("=" * 50)
    print("🤖 AI-Powered HOI4 Code Generation")
    print("📝 Uses OpenAI GPT-4o for intelligent scripting")
    print()
    
    if hoi4_generator is None:
        print("⚠️  CONFIGURATION REQUIRED:")
        print("1. Copy config/config.json.template to config/config.json")
        print("2. Add your OpenAI API key to config/config.json")
        print("3. Restart the application")
        print()
    
    print("🚀 Starting server...")
    print("📱 Open your browser and navigate to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000) 