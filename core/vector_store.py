"""
VectorStore - Career Role and Skills Database
A simple but powerful vector store for searching career roles by skills and role names.
"""

import asyncio
from typing import List, Dict, Optional


class VectorStore:
    """
    Vector store for career roles and their associated skills.
    Supports async initialization and keyword-based search.
    """
    
    def __init__(self):
        """Initialize the vector store with comprehensive career data"""
        self.data = [
            # Software Engineering Roles
            {"role": "Frontend Engineer", "skills": ["JavaScript", "React", "CSS", "HTML", "Vue.js"]},
            {"role": "Backend Engineer", "skills": ["Python", "Node.js", "Java", "Databases", "APIs"]},
            {"role": "Full Stack Engineer", "skills": ["JavaScript", "Python", "React", "Databases", "Docker"]},
            {"role": "DevOps Engineer", "skills": ["Docker", "Kubernetes", "AWS", "CI/CD", "Linux"]},
            {"role": "Cloud Architect", "skills": ["AWS", "Azure", "GCP", "Architecture", "Security"]},
            {"role": "Database Administrator", "skills": ["SQL", "MongoDB", "PostgreSQL", "Backup", "Performance Tuning"]},
            {"role": "Systems Engineer", "skills": ["Linux", "Networking", "Infrastructure", "Troubleshooting", "Automation"]},
            {"role": "Security Engineer", "skills": ["Cybersecurity", "Encryption", "Firewalls", "Penetration Testing", "Security Protocols"]},
            {"role": "QA Engineer", "skills": ["Testing", "Selenium", "Bug Tracking", "Test Automation", "Quality Assurance"]},
            {"role": "Mobile Developer", "skills": ["React Native", "Swift", "Kotlin", "Mobile Design", "App Development"]},
            
            # Data & AI Roles
            {"role": "ML Engineer", "skills": ["Python", "Machine Learning", "TensorFlow", "PyTorch", "Deep Learning"]},
            {"role": "Data Scientist", "skills": ["Python", "Statistics", "SQL", "Pandas", "Data Analysis"]},
            {"role": "Data Engineer", "skills": ["Python", "SQL", "Spark", "ETL", "Data Pipelines"]},
            {"role": "Analytics Engineer", "skills": ["SQL", "dbt", "Data Warehousing", "Analytics", "Reporting"]},
            {"role": "AI Researcher", "skills": ["Machine Learning", "Mathematics", "Research", "Python", "Deep Learning"]},
            {"role": "NLP Engineer", "skills": ["NLP", "Python", "NLTK", "Transformers", "Deep Learning"]},
            {"role": "Computer Vision Engineer", "skills": ["OpenCV", "Python", "Deep Learning", "Image Processing", "CNNs"]},
            {"role": "Analytics Manager", "skills": ["Data Analysis", "Leadership", "SQL", "Tableau", "Strategy"]},
            {"role": "Data Analyst", "skills": ["SQL", "Excel", "Tableau", "Data Analysis", "Business Intelligence"]},
            {"role": "Business Intelligence Developer", "skills": ["SQL", "Power BI", "Tableau", "ETL", "Data Modeling"]},
            
            # Product & Design Roles
            {"role": "Product Manager", "skills": ["Product Strategy", "Leadership", "Analytics", "Communication", "Roadmapping"]},
            {"role": "Product Designer", "skills": ["UI Design", "UX Research", "Figma", "Prototyping", "User Testing"]},
            {"role": "UX Designer", "skills": ["User Research", "Wireframing", "Prototyping", "Figma", "Design Systems"]},
            {"role": "UI Designer", "skills": ["Visual Design", "Figma", "Adobe Creative Suite", "Design Systems", "Branding"]},
            {"role": "Design Systems Manager", "skills": ["Design Systems", "Component Design", "Documentation", "Leadership", "Design"]},
            {"role": "Interaction Designer", "skills": ["Prototyping", "Animation", "UX", "Figma", "User Experience"]},
            {"role": "UX Researcher", "skills": ["User Research", "Data Analysis", "Qualitative Research", "Testing", "Insights"]},
            
            # Business & Sales Roles
            {"role": "Sales Manager", "skills": ["Sales", "Leadership", "Negotiation", "CRM", "Team Management"]},
            {"role": "Account Executive", "skills": ["Sales", "Client Relations", "CRM", "Negotiation", "Communication"]},
            {"role": "Business Development Manager", "skills": ["Sales", "Strategy", "Networking", "Partnership", "Growth"]},
            {"role": "Solutions Architect", "skills": ["Technical Knowledge", "Problem Solving", "Presentation", "Sales", "Architecture"]},
            {"role": "Sales Engineer", "skills": ["Technical Knowledge", "Sales", "Demonstrations", "Client Relations", "Problem Solving"]},
            {"role": "Account Manager", "skills": ["Client Relations", "Communication", "CRM", "Sales", "Relationship Management"]},
            {"role": "Business Analyst", "skills": ["Data Analysis", "Problem Solving", "Communication", "Requirements", "Documentation"]},
            
            # Marketing & Content Roles
            {"role": "Product Marketing Manager", "skills": ["Marketing", "Product Knowledge", "Content Writing", "Analytics", "Strategy"]},
            {"role": "Marketing Manager", "skills": ["Marketing", "Strategy", "Analytics", "Content", "Campaign Management"]},
            {"role": "Content Strategist", "skills": ["Content Writing", "SEO", "Analytics", "Copywriting", "Strategy"]},
            {"role": "SEO Specialist", "skills": ["SEO", "Content Writing", "Analytics", "Keyword Research", "Technical SEO"]},
            {"role": "Social Media Manager", "skills": ["Social Media", "Content Creation", "Analytics", "Engagement", "Copywriting"]},
            {"role": "Email Marketing Specialist", "skills": ["Email Marketing", "Copywriting", "Analytics", "Segmentation", "Automation"]},
            {"role": "Content Writer", "skills": ["Writing", "Research", "SEO", "Editing", "Communication"]},
            {"role": "Technical Writer", "skills": ["Technical Writing", "Documentation", "Clarity", "Research", "Tools"]},
            
            # Leadership & Management Roles
            {"role": "Engineering Manager", "skills": ["Leadership", "Technical Knowledge", "Team Management", "Mentoring", "Strategy"]},
            {"role": "Director of Engineering", "skills": ["Leadership", "Strategy", "Architecture", "Team Management", "Vision"]},
            {"role": "VP of Engineering", "skills": ["Leadership", "Strategic Vision", "Architecture", "Organizational Design", "Execution"]},
            {"role": "Chief Technology Officer", "skills": ["Leadership", "Strategy", "Architecture", "Vision", "Decision Making"]},
            {"role": "Product Lead", "skills": ["Product Strategy", "Leadership", "Vision", "Communication", "Roadmapping"]},
            {"role": "Engineering Lead", "skills": ["Leadership", "Technical Knowledge", "Mentoring", "Communication", "Architecture"]},
            {"role": "Team Lead", "skills": ["Leadership", "Mentoring", "Communication", "Technical Knowledge", "Problem Solving"]},
            
            # Finance & Operations Roles
            {"role": "Financial Analyst", "skills": ["Financial Analysis", "Excel", "Data Analysis", "Forecasting", "Reporting"]},
            {"role": "Accountant", "skills": ["Accounting", "Excel", "Financial Reporting", "Tax", "QuickBooks"]},
            {"role": "Operations Manager", "skills": ["Operations", "Process Improvement", "Leadership", "Analytics", "Organization"]},
            {"role": "Finance Manager", "skills": ["Financial Management", "Budget Planning", "Leadership", "Analysis", "Reporting"]},
            {"role": "Procurement Specialist", "skills": ["Procurement", "Vendor Management", "Negotiation", "Cost Control", "Communication"]},
            
            # Human Resources Roles
            {"role": "HR Manager", "skills": ["HR", "Recruitment", "Employee Relations", "Leadership", "Communication"]},
            {"role": "Recruiter", "skills": ["Recruitment", "Communication", "Networking", "Interviewing", "ATS"]},
            {"role": "People Operations Manager", "skills": ["HR", "Operations", "Employee Experience", "Analytics", "Organization"]},
            {"role": "Learning & Development Manager", "skills": ["Training", "Development", "Leadership", "Communication", "Content Creation"]},
            
            # Legal & Compliance Roles
            {"role": "Lawyer", "skills": ["Legal Knowledge", "Contract Law", "Research", "Communication", "Writing"]},
            {"role": "Compliance Officer", "skills": ["Compliance", "Regulation", "Risk Management", "Audit", "Documentation"]},
            
            # Education & Training Roles
            {"role": "Software Engineer Trainer", "skills": ["Teaching", "Technical Knowledge", "Communication", "Curriculum Design", "Mentoring"]},
            {"role": "Data Science Trainer", "skills": ["Teaching", "Data Science", "Communication", "Python", "Curriculum Design"]},
            {"role": "Technical Instructor", "skills": ["Teaching", "Technical Knowledge", "Communication", "Curriculum", "Training"]},
            
            # Consulting Roles
            {"role": "Management Consultant", "skills": ["Consulting", "Strategy", "Analysis", "Communication", "Problem Solving"]},
            {"role": "Technology Consultant", "skills": ["Consulting", "Technical Knowledge", "Strategy", "Problem Solving", "Communication"]},
            
            # Creative & Design Roles
            {"role": "Brand Manager", "skills": ["Branding", "Strategy", "Communication", "Marketing", "Creative Thinking"]},
            {"role": "Creative Director", "skills": ["Creative Direction", "Leadership", "Design", "Strategy", "Vision"]},
            {"role": "Graphic Designer", "skills": ["Graphic Design", "Adobe Creative Suite", "Branding", "Visual Design", "Creativity"]},
            {"role": "Motion Designer", "skills": ["Animation", "Motion Graphics", "Adobe Creative Suite", "Design", "Creativity"]},
            
            # Infrastructure & DevOps
            {"role": "Infrastructure Engineer", "skills": ["Infrastructure", "AWS", "Networking", "Linux", "Automation"]},
            {"role": "Release Manager", "skills": ["Release Management", "Deployment", "Automation", "Documentation", "Communication"]},
            {"role": "Network Engineer", "skills": ["Networking", "Infrastructure", "Security", "Troubleshooting", "Linux"]},
            
            # Support & Customer Success
            {"role": "Customer Success Manager", "skills": ["Customer Relations", "Communication", "Problem Solving", "Product Knowledge", "Analytics"]},
            {"role": "Customer Support Engineer", "skills": ["Technical Support", "Problem Solving", "Communication", "Customer Relations", "Documentation"]},
            {"role": "Support Manager", "skills": ["Leadership", "Customer Relations", "Problem Solving", "Communication", "Team Management"]},
            
            # Partnership & Ecosystem
            {"role": "Partner Manager", "skills": ["Partnership", "Relationship Management", "Negotiation", "Communication", "Strategy"]},
            {"role": "Developer Relations Manager", "skills": ["Developer Relations", "Technical Knowledge", "Communication", "Community Building", "Strategy"]},
            
            # Research & Innovation
            {"role": "Research Scientist", "skills": ["Research", "Machine Learning", "Mathematics", "Python", "Publication"]},
            {"role": "Innovation Manager", "skills": ["Innovation", "Strategy", "Problem Solving", "Creativity", "Leadership"]},
            
            # Quality & Testing
            {"role": "Test Automation Engineer", "skills": ["Test Automation", "Selenium", "Python", "QA", "Scripting"]},
            {"role": "Quality Assurance Manager", "skills": ["QA", "Leadership", "Testing Strategy", "Team Management", "Quality"]},
            
            # Additional Specialized Roles
            {"role": "Growth Manager", "skills": ["Growth Strategy", "Analytics", "Experimentation", "Data Analysis", "Communication"]},
            {"role": "Product Operations Manager", "skills": ["Product Operations", "Analytics", "Process Improvement", "Documentation", "Communication"]},
            {"role": "Security Architect", "skills": ["Security", "Architecture", "Risk Management", "Strategy", "Technical Knowledge"]},
            {"role": "Infrastructure Architect", "skills": ["Infrastructure", "Architecture", "AWS", "Design", "Strategy"]},
            {"role": "Data Architect", "skills": ["Data Architecture", "Database Design", "Scalability", "SQL", "Strategy"]},
            {"role": "Enterprise Architect", "skills": ["Enterprise Architecture", "Strategy", "Design", "Integration", "Leadership"]},
            {"role": "Blockchain Developer", "skills": ["Blockchain", "Solidity", "Cryptocurrency", "Smart Contracts", "Python"]},
            {"role": "Embedded Systems Engineer", "skills": ["C++", "Embedded Systems", "Hardware", "Firmware", "Microcontrollers"]},
            {"role": "Game Developer", "skills": ["Game Development", "Unity", "Unreal Engine", "C#", "3D Graphics"]},
            {"role": "AR/VR Developer", "skills": ["AR/VR", "Unity", "3D Development", "C#", "User Experience"]},
            {"role": "ML Ops Engineer", "skills": ["Machine Learning", "DevOps", "Python", "Model Deployment", "Monitoring"]},
            {"role": "Robotics Engineer", "skills": ["Robotics", "C++", "Computer Vision", "Hardware", "Control Systems"]},
            {"role": "Site Reliability Engineer", "skills": ["SRE", "Monitoring", "Infrastructure", "Linux", "Automation"]},
            {"role": "Quantum Developer", "skills": ["Quantum Computing", "Python", "Quantum Algorithms", "Mathematical Knowledge"]},
        ]
        self.is_initialized = False
    
    async def initialize(self) -> None:
        """
        Async initialization of the vector store.
        In a real implementation, this would load embeddings and prepare the index.
        """
        try:
            # Simulate async initialization (could load embeddings from DB, file, etc.)
            await asyncio.sleep(0.1)
            self.is_initialized = True
            print(f"✅ VectorStore initialized with {len(self.data)} career roles")
        except Exception as e:
            print(f"❌ Error initializing VectorStore: {e}")
            raise
    
    async def search(self, query: str, limit: int = 5) -> List[Dict[str, any]]:
        """
        Search the vector store for matching careers based on keywords.
        
        Args:
            query (str): Search query (role name or skill)
            limit (int): Maximum number of results to return (default: 5)
        
        Returns:
            List[Dict]: List of matching career roles with skills
        """
        if not self.is_initialized:
            print("⚠️  VectorStore not initialized. Call await initialize() first.")
            return []
        
        query_lower = query.lower().strip()
        
        if not query_lower:
            return self.data[:limit]
        
        matches = []
        
        # Search through all careers
        for career in self.data:
            role_name = career["role"].lower()
            skills = [skill.lower() for skill in career["skills"]]
            
            # Check if query matches role name (exact or partial)
            if query_lower in role_name:
                matches.append((career, 2))  # Role match has higher priority
            # Check if query matches any skill
            elif any(query_lower in skill for skill in skills):
                matches.append((career, 1))  # Skill match has lower priority
        
        # Sort by priority (role matches first, then skill matches)
        matches.sort(key=lambda x: x[1], reverse=True)
        
        # Return top matches
        results = [match[0] for match in matches]
        return results[:limit] if results else self.data[:limit]
    
    async def search_by_skills(self, skills: List[str], limit: int = 5) -> List[Dict[str, any]]:
        """
        Search for careers that match multiple skills.
        
        Args:
            skills (List[str]): List of skills to search for
            limit (int): Maximum number of results to return
        
        Returns:
            List[Dict]: List of careers that match the skills
        """
        if not self.is_initialized:
            print("⚠️  VectorStore not initialized. Call await initialize() first.")
            return []
        
        skills_lower = [skill.lower().strip() for skill in skills]
        matches = []
        
        for career in self.data:
            career_skills = [skill.lower() for skill in career["skills"]]
            # Count how many skills match
            skill_matches = sum(1 for skill in skills_lower if any(skill in cs for cs in career_skills))
            
            if skill_matches > 0:
                matches.append((career, skill_matches))
        
        # Sort by number of matching skills
        matches.sort(key=lambda x: x[1], reverse=True)
        
        results = [match[0] for match in matches]
        return results[:limit] if results else []
    
    def get_all_roles(self) -> List[str]:
        """Get all available role names"""
        return [career["role"] for career in self.data]
    
    def get_all_skills(self) -> List[str]:
        """Get all unique skills in the database"""
        skills = set()
        for career in self.data:
            skills.update(career["skills"])
        return sorted(list(skills))
    
    def get_role_by_name(self, role_name: str) -> Optional[Dict[str, any]]:
        """Get a specific role by its exact name"""
        for career in self.data:
            if career["role"].lower() == role_name.lower():
                return career
        return None


# ============================================================================
# Example Usage and Testing
# ============================================================================

async def main():
    """Demo function showing how to use the VectorStore"""
    
    # Create and initialize the vector store
    vector_store = VectorStore()
    await vector_store.initialize()
    
    # Example 1: Search by role name
    print("\n" + "="*60)
    print("SEARCH BY ROLE NAME: 'Engineer'")
    print("="*60)
    results = await vector_store.search("Engineer", limit=3)
    for result in results:
        print(f"  • {result['role']}")
        print(f"    Skills: {', '.join(result['skills'][:3])}...")
    
    # Example 2: Search by skill
    print("\n" + "="*60)
    print("SEARCH BY SKILL: 'Python'")
    print("="*60)
    results = await vector_store.search("Python", limit=3)
    for result in results:
        print(f"  • {result['role']}")
        print(f"    Skills: {', '.join(result['skills'][:3])}...")
    
    # Example 3: Search by multiple skills
    print("\n" + "="*60)
    print("SEARCH BY MULTIPLE SKILLS: ['Python', 'SQL', 'Leadership']")
    print("="*60)
    results = await vector_store.search_by_skills(["Python", "SQL", "Leadership"], limit=3)
    for result in results:
        print(f"  • {result['role']}")
        print(f"    Skills: {', '.join(result['skills'][:3])}...")
    
    # Example 4: Get statistics
    print("\n" + "="*60)
    print("VECTOR STORE STATISTICS")
    print("="*60)
    print(f"  Total Roles: {len(vector_store.get_all_roles())}")
    print(f"  Total Unique Skills: {len(vector_store.get_all_skills())}")
    print(f"  Sample Skills: {', '.join(vector_store.get_all_skills()[:5])}")
    
    # Example 5: Get specific role
    print("\n" + "="*60)
    print("GET SPECIFIC ROLE: 'ML Engineer'")
    print("="*60)
    role = vector_store.get_role_by_name("ML Engineer")
    if role:
        print(f"  Role: {role['role']}")
        print(f"  Skills: {', '.join(role['skills'])}")


if __name__ == "__main__":
    asyncio.run(main())