from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base