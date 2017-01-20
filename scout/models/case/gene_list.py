# -*- coding: utf-8 -*-
from mongoengine import (Document, ListField, StringField, FloatField,
                         DateTimeField, BooleanField, EmbeddedDocument,
                         EmbeddedDocumentField, MapField, ReferenceField,
                         IntField, SortedListField)

from scout.models.hgnc_map import HgncGene


class Gene(EmbeddedDocument):

    meta = {'strict': False}

    hgnc_gene = ReferenceField(HgncGene, required=True)

    disease_associated_transcripts = ListField(StringField())
    reduced_penetrance = BooleanField(default=False)
    mosaicism = BooleanField(default=False)
    database_entry_version = StringField()

    def __unicode__(self):
        return "{this.hgnc_gene.hgnc_symbol}".format(this=self)


class GeneMeta(EmbeddedDocument):
    hgnc_id = IntField()
    symbol = StringField()

    def __unicode__(self):
        return "{this.hgnc_id}: {this.symbol}".format(this=self)


class GenePanel(Document):

    meta = {'strict': False}

    panel_name = StringField(required=True, unique_with='version')
    institute = StringField()
    version = FloatField(required=True)
    date = DateTimeField(required=True)
    display_name = StringField()
    # This is a dictionary with gene objects
    gene_objects = MapField(EmbeddedDocumentField(Gene))
    # {'ADK':Gene}
    genes = SortedListField(EmbeddedDocumentField(GeneMeta), ordering='symbol')

    @property
    def gene_ids(self):
        for gene in self.genes:
            yield gene.hgnc_id

    @property
    def gene_symbols(self):
        for gene in self.genes:
            yield gene.symbol

    @property
    def name_and_version(self):
        """Return the name of the panel and version."""
        return "{this.display_name} ({this.version})".format(this=self)

    def __unicode__(self):
        return "{this.panel_name} ({this.version})".format(this=self)

    def __repr__(self):
        return ("GeneList(name={0}, version={1}, date={2}, display_name={3})"
                .format(self.panel_name, self.version, self.date,
                        self.display_name))
