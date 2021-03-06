# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from haystack import indexes
from haystack import site
from dormbase.core.models import *

class ResidentIndex(indexes.SearchIndex):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    firstname = indexes.EdgeNgramField(model_attr='user__first_name')
    lastname = indexes.EdgeNgramField(model_attr='user__last_name')
    title  = indexes.EdgeNgramField(model_attr='title')
    username = indexes.EdgeNgramField(model_attr='athena')
    room = indexes.EdgeNgramField(model_attr='room__number')
    year = indexes.IntegerField(model_attr='year')
    
    def get_model(self):
        return Resident

    def index_queryset(self):
        return self.get_model().objects

site.register(Resident, ResidentIndex)
